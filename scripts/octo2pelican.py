#coding=utf-8
#!/usr/bin/env python

import os
import datetime
from collections import OrderedDict

import yaml
import html2text

__doc__ = 'A quick script for converting octopress posts (markdown source files) to pelican posts'


# configure following variables according to your blog
blog_author = 'alswl'

# a sorted order of metadata for consistency
metadata_order = ['Title', 'Author', 'Slug', 'Date', 'Tags', 'Category',
                  'Summary', 'Status']


def is_md(f):
    return os.path.splitext(f)[1] in ('.md', '.markdown')

def is_html(f):
    return os.path.splitext(f)[1] in ('.html',)

def octopress_files(path):
    return (os.path.join(path, f) for f in os.listdir(path) if is_md(f) or is_html(f))


def parse(lines):
    """Parses lines of an octopress markdown file and returns an un-named
    tuple of metadata dict and body of the post in that order

    """
    in_yaml = False
    metadata = []
    body = []
    for line in lines:
        if line == '---' and not in_yaml:
            in_yaml = True
        elif line == '---' and in_yaml:
            in_yaml = False
        elif in_yaml:
            metadata.append(line)
        else:
            body.append(line)
    return (yaml.load('\n'.join(metadata)), '\n'.join(body))


def pelicanize(filepath):
    """Takes a path to octopress post file and `pelicanizes` it. Returns
    an un-named tuple of the pelican post filename and the post in
    that order

    """
    with open(filepath) as f:
        lines = (line.decode('utf-8').rstrip('\n') for line in f)
        yml, content = parse(lines)
        metadata = pelicanize_metadata(yml, filepath)
        if is_md(filepath):
            body = pelicanize_body(content)
        elif is_html(filepath):
            body = pelicanize_html_body(content)
        else:
            raise ValueError()
        content = ''
        for k, v in metadata.iteritems():
            content += '%s: %s\n' % (k, v)
        content += '\n'
        content += body
    filename = pelicanize_filename(os.path.basename(filepath))
    return (filename, content)


def pelicanize_filename(filename):
    """Gets rid of date portion in the octopress filenames"""
    name, ext = os.path.splitext(filename)
    return '%s.md' %name


def pelicanize_metadata(metadata, filepath):
    """Converts the octopress style metadata (yaml in md files) to pelican
    style metadata.

    Basically, removes unnecessary data, capitalizes the keys and
    sorts in a standard order (not a pelican requirement, but rather
    to maintain consistency)

    """
    filename = os.path.split(filepath)[1]
    not_required = ('layout', 'link', 'categories', 'comments', 'published')
    new_metadata = dict([(k, ', '.join(v) if type(v)==list else v)
                     for k, v in metadata.iteritems()
                     if k not in not_required])
    new_metadata['date'] = str(metadata.get('date') or
                           os.path.splitext(filename)[0][0:10] + ' 00:00:00')
    new_metadata['Summary'] = ''
    new_metadata['Author'] = blog_author
    if 'categories' in metadata:
        if isinstance(metadata['categories'], list):
            new_metadata['Category'] = ', '.join(metadata['categories'])
        else:
            new_metadata['Category'] = metadata['categories']
    if 'published' in metadata:
        if metadata['published'] == False:
            new_metadata['status'] = 'draft'
    new_metadata['slug'] = os.path.splitext(filename)[0][11:]
    meta = dict(zip(map(str.capitalize, new_metadata.keys()),
                    new_metadata.values()))

    return OrderedDict(sorted(meta.items(), 
                              cmp=lambda x, y: cmp(metadata_order.index(x[0]),
                                                   metadata_order.index(y[0]))))


def pelicanize_body(body):
    return body

def pelicanize_html_body(body):
    return html2text.html2text(body)

def test():
    orig = '2012-05-04-own-the-editor.markdown'
    assert pelicanize_filename(orig) == 'own-the-editor.md'

    octo_meta = {'categories': ['jquery', 'javascript'],
                 'comments': True,
                 'date': datetime.datetime(2009, 8, 23, 23, 47, 23),
                 'layout': 'post',
                 'link': 'http://vineetnaik.me/blog/2009/08/a-self-made-jquery-slider/',
                 'published': True,
                 'tags': ['jquery',
                          'slider',
                          'image gallery'],
                 'title': 'A self made Jquery slider'}
    pelican_meta = pelicanize_metadata(octo_meta)
    for k in ('comments', 'layout', 'link', 'published'):
        assert not k in pelican_meta

    assert pelican_meta['Category'] == 'jquery, javascript'
    assert pelican_meta['Tags'] == 'jquery, slider, image gallery'
    assert pelican_meta['Title'] == 'A self made Jquery slider'
    assert pelican_meta['Date'] == '2009-08-23 23:47:23'
    assert pelican_meta['Author'] == blog_author
    
    print 'All tests pass.'    


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-s', '--source', required=True, help='Source dir or path to the octopress source files')
    parser.add_argument('-t', '--target', required=True, help='Target dir or path to the output directory')
    args = parser.parse_args()

    source_files = octopress_files(args.source)

    pelican_posts = []
    for f in source_files:
        try:
            pelican_posts.append(pelicanize(f))
        except Exception, e:
            print e
            continue
    for (filename, post) in pelican_posts:
        print filename
        with open(os.path.join(args.target, filename), 'w') as f:
            f.write(post.encode('utf-8'))
    
