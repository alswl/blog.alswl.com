# coding=utf-8

import re
import requests
import os

def process_line(row):
    #import ipdb; ipdb.set_trace()
    base_dir = '/Users/alswl/t1/uploads/'
    file = re.search('content/.*.md', row).group()
    url = re.search(r'http://[^\)]+', row).group()
    year, month = re.search(r'content/(\d+)-(\d+)', file).groups()
    file_name = url.split('/')[-1].lower()

    to_file = base_dir + '%s%s/%s' % (year, month, file_name)


    if not os.path.isfile(to_file):
        resp = requests.get(url, timeout=2)
        if resp.status_code != 200:
            raise ValueError(url)
        try:
            os.mkdir(base_dir + '%s%s' % (year, month))
        except:
            pass
        with open(to_file, 'wb') as f:
            f.write(resp.content)
    with open(file, 'r+') as f:
        origin = f.read()
        new = origin.replace(url, 'http://upload.log4d.com/upload_dropbox/%s%s/%s' % (year, month, file_name))
        f.seek(0)
        f.truncate(0)
        f.write(new)

def main():
    rows = """
content/2009-07-19-those-times-those-who-do-log-archiving-2006.md:154:![image](http://tk.files.storage.msn.com/x1pUr2osLO3XWgOPrtg08dwnT2RFheAhyvCbmwwzPCwoV_FOKBabn57wzaidHMpUiBmEYWq1dcNbUdZ7iBSDJ4JggYY6-Pok8RJXY4TJsWPzwkhP4Jbll-12d6kkKKJ_Dj4RS5gY7mhrjc)
content/2009-07-19-those-times-those-who-do-log-archiving-2006.md:179:![image](http://tk.files.storage.msn.com/x1pUr2osLO3XWgOPrtg08dwnSM5oHSgLwSOttbWBKJK7g3HvF_JgzWquU_o6MUTJHi9RjoqTF6wTVeSbR4828UZD5eCdbgd5gEvhhuihCO_FIJqbtCfJluGoetLVeCAp09ayrS8qYVfr3Q)
content/2009-07-19-those-times-those-who-do-log-archiving-2006.md:189:![image](http://tk.files.storage.msn.com/x1pUr2osLO3XWgOPrtg08dwnREMVJeMGraLFaT_9b6RcvTphyc3TK2T0js4OKMcP6B858TR0l9xNWmyJydZAAdEcGo8hZoiA-LEUi2lPQc9tMirxFvtF2R67p0XeDYcok4OtuI7abKL3is)
content/2009-07-19-those-times-those-who-do-log-archiving-2006.md:191:![image](http://tk.files.storage.msn.com/x1pUr2osLO3XWgOPrtg08dwnVuDkImqT6GmMInndYm9xk3lBDJemEbvoCIGZmMefgOWt0eDxAxxuqZhfURrMlugId6CWCe5D2detLXYVxtXsvVELGuKvoj92FqFAKr5noAAC3jprtEthF0)
content/2009-07-19-those-times-those-who-do-log-archiving-2006.md:208:![image](http://tk.files.storage.msn.com/x1pUr2osLO3XWgOPrtg08dwnZBQ_3LvJWOocb6hYBJYDv8uJJkz6mxcukOFLGQiDmSet6v5HW2vssPHSI093Azv8qLV__MZqZRuwjJ5wIa0N9HHdShEtpHj-JnvJL55o1SX) 那个,很感谢堕堕留言,仔细看一下,好像就这么一个人在留言,(脸红一下),你们的Space那么漂亮,还有那个羽化.没关系,继续努力.
content/2009-07-19-those-times-those-who-do-log-archiving-2006.md:226:为了最大限度榨干奸商每一分利润,不让他骗取我一分钱,我特地做了一份买手机策划书.如下. ![image](http://tkfiles.storage.msn.com/x1pUr2osLO3XWgOPrtg08dwnYjGBdoTAaMW0VjyR8Rp0gyApwO5ITsl0KJty4hpCDZ1xKCZRFynfmNApNyARXBQkPKzC2QeCbr2UAIq74FIeVP0wuqK_Vhb6AtatdM5stKKVssvRh0xoaU)最后,坚决不让卖手机的那
content/2009-07-19-those-times-those-who-do-log-archiving-2006.md:273:这本日记第一篇日记是1997-2-21,最后一篇是1999-6-22. ![image](http://tkfiles.storage.msn.com/x1p4JHjVbcjTC-ewUafvAHFbEJuBX7Eu85QPe3cvLmL4Sw25YJ0XDsR45PFn0_bXu2YYWeT20b5Q6GE93CH_ECG15ZwDE4p0D6X4UZVpRY3CJZF2hdWNf_IUTodw6rbA9uf1l61aE45SJdjaho2tCWm4A)
content/2009-07-19-those-times-those-who-do-log-archiving-2006.md:275:![image](http://tkfiles.storage.msn.com/x1p4JHjVbcjTC-ewUafvAHFbEJuBX7Eu85QPe3cvLmL4Sz5z8EV45WocJ7v8qDPkRhk_oih-UrH-hyycKj6OadNXG3eJtjSZ1nOZofoJdwQnJS6ljlrFm6KRBzQcgwCzkgzs_6XnrQThvU7PFidyzFGkg)
content/2009-07-19-those-times-those-who-do-log-archiving-2006.md:481:![image](http://tkfiles.storage.msn.com/x1pUr2osLO3XWgOPrtg08dwnfd5FRo6Z9yUPoCBurJBS0vKTE0rXjGJfpZQylXGHfJCMaG7bDg3vg8SYatRUReUih4FgvRNyvQwU0yUd8Pba_dt8UAAFOyc03UgISZkWJJ_TIFyLGQfYws)
content/2009-10-11-lonely-root-of-3.md:14:[caption id="" align="alignnone" width="306" caption="爱情公寓"][![爱情公寓](http://img3.doubanio.com/lpic/s3940602.jpg)](http://img3.doubanio.com/lpic/s3940602.jpg)[/caption
content/2009-11-16-getting-started-with-java-books-java-jdk6-study-notes.md:8:[![Java JDK6学习笔记](http://img3.doubanio.com/lpic/s2518833.jpg)](http://img3.doubanio.com/
content/2010-01-30-development-of-cross-browser-javascript-should-pay-attention-to-the-problem.md:19:![image](http://img3.doubanio.com/lpic/s3651235.jpg)
content/2010-03-19-guide-to-find-a-wordpress-syntax-highlighter-that-works-translation.md:53:[![p06-syntax-highlighter-evolved](http://www.travislin.com/wp-content/uploads/2009/05/p06-syntax-highlighter-evolved-300x269.gif)](http://www.travislin.com/wp-content/uploads/2009/05/p06-syntax-highlighter-evolved.gif)
content/2010-03-19-guide-to-find-a-wordpress-syntax-highlighter-that-works-translation.md:55:[![p06-syntax-highlighter-evolved-02](http://www.travislin.com/wp-content/uploads/2009/05/p06-syntax-highlighter-evolved-02-300x157.gif)](http://www.travislin.com/wp-content/uploads/2009/05/p06-syntax-highlighter-evolved-02.gif)
content/2010-03-19-guide-to-find-a-wordpress-syntax-highlighter-that-works-translation.md:67:[![p06-syntax-highlighter-plus](http://www.travislin.com/wp-content/uploads/2009/05/p06-syntax-highlighter-plus-287x300.gif)](http://www.travislin.com/wp-content/uploads/2009/05/p06-syntax-highlighter-plus.gif)
content/2010-03-19-guide-to-find-a-wordpress-syntax-highlighter-that-works-translation.md:80:[![p06-google-syntax-lighlighter](http://www.travislin.com/wp-content/uploads/2009/05/p06-google-syntax-lighlighter-275x300.gif)](http://www.travislin.com/wp-content/uploads/2009/05/p06-google-syntax-lighlighter.gif)
content/2010-03-19-guide-to-find-a-wordpress-syntax-highlighter-that-works-translation.md:82:[![p06-google-syntax-lighlighter-02](http://www.travislin.com/wp-content/uploads/2009/05/p06-google-syntax-lighlighter-02-300x162.gif)](http://www.travislin.com/wp-content/uploads/2009/05/p06-google-syntax-lighlighter-02.gif)
content/2010-04-07-ui-design-tool-balsamiq-mockups.md:43:![balsamiq markup exported to png](http://farm4.static.flickr.com/3451/3179518230_5ec1947cb9_m.jpg)
content/2010-04-17-recently-read-books.md:12:![image](http://img3.doubanio.com/mpic/s1429078.jpg)
content/2010-04-17-recently-read-books.md:44:![image](http://img3.doubanio.com/mpic/s1086045.jpg)
content/2010-04-17-recently-read-books.md:53:![image](http://img3.doubanio.com/mpic/s4271706.jpg)
content/2010-07-09-sms-backup-for-android.md:58:![01-Android-SMS-Backup](http://orzhd.com/briian/2009/AndroidSMSBackupGmail_12DB8/01AndroidSMSBackup.png)
content/2010-08-18-cook-book.md:18:![image](http://img3.doubanio.com/lpic/s3174468.jpg)
content/2014-02-23-redis-benchmarks.md:212:![Data size impact](https://raw.githubusercontent.com/dspezia/redis-doc/client_command/topics/Data_size.png)
content/2014-02-23-redis-benchmarks.md:222:![NUMA chart](https://raw.githubusercontent.com/dspezia/redis-doc/6374a07f93e867353e5e946c1e39a573dfc83f6c/topics/NUMA_chart.gif)
content/2014-02-23-redis-benchmarks.md:229:![connections chart](https://raw.githubusercontent.com/dspezia/redis-doc/system_info/topics/Connections_chart.png)

    """

    for row in rows.splitlines():
        try:
            process_line(row)
        except Exception as e:
            print('X: %s' % row)
            print(e)
            continue
        print('V: %s' % row)


if __name__ == '__main__':
    main()
