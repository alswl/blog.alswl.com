Title: Java写的Mp3歌词复制器
Author: alswl
Slug: lyrics-written-in-java-replicator-mp3
Date: 2009-05-25 00:00:00
Tags: 
Category: Java

大家可能会遇到这样的情况，Mp3里有很多歌，电脑上也有很多相同的歌，但是有歌词。把歌词同步到Mp3播放器非常麻烦，我以前用千千静听导入目录，然后逐个播放，或
者用一个软件从网上搜索到Mp3播放器。 千千静听或者其他播放器都会有一个选项是设置歌词存储位置的，一般来说，我们听过的歌都是会自动下载歌词到这个文件夹，其实
我们完全可以不必大费周折去找lrc，只要把这个歌词文件夹和Mp3播放器同步就可以了。
以前就想写一个东西完成这个麻烦的工程，现在贴吧1.0完成了，可以休息几天，晚上花了一点时间用Java写了一个这样的小东西。
如果大家碰到和我一样的麻烦，可以试试。呃，时间仓促，没有图形界面，而且必须是Java程序员才能用，因为我这儿只提供了源码....

    
    package ddd;

import java.io.BufferedReader;

import java.io.File;

import java.io.IOException;

import java.io.InputStreamReader;

public class App {

/**

* @author alswl  
* @site dddspace.cn  
* @param args  
* @throws IOException  
*/  
public static void main(String[] args) throws IOException {

String pathMp3;

String pathLrc;

BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

print("请输入Mp3根目录");

pathMp3 = in.readLine();

print("请输入Lrc目录");

pathLrc = in.readLine();

copyLrc(pathMp3, pathLrc);

}

private static void copyLrc(String mp3sPath, String lrcsPath) {

String pathMp3 = mp3sPath;

String pathLrc = lrcsPath;

File folderMp3 = new File(pathMp3);

File folderLrc = new File(pathLrc);

if (!folderMp3.isDirectory() || !folderLrc.isDirectory()) {

print("文件夹错误");

return;

}

File[] mp3s = folderMp3.listFiles();

File[] lrcs = folderLrc.listFiles();

for (File mp3 : mp3s) {

if (mp3.isDirectory()) {

copyLrc(mp3.toString(), lrcsPath);

} else {

for (File lrc : lrcs) {

String mp3Name = mp3.getName().substring(0,

mp3.getName().length() - 4);

String lrcName = lrc.getName().substring(0,

lrc.getName().length() - 4);

if (mp3Name.equals(lrcName)) {

print("!" + lrc.toString() + "to "

+ folderMp3.toString());

runCmd(""" + lrc.toString() + """, """

+ folderMp3.toString() + """);

}

}

}

}

}

private static void print(Object s) {

System.out.println(s);

}

private static void runCmd(String s1, String s2) {

Runtime rt = Runtime.getRuntime();

try {

rt.exec("cmd /c copy " + s1 + " " + s2);

} catch (Exception e) {

e.printStackTrace();

}

}

}

09_05_26新增 jar格式的可执行文件链接，[猛击这里打开](http://log4d.com/2009/05/26/the-executable-
file-mp3lrc)

