Title: Ubuntu安装之后设定操作
Author: alswl
Slug: ubuntu-setup
Date: 2011-04-07 00:00:00
Tags: Linuxer, Ubuntu
Category: Coding

前几天使用chmod时候，多打了一个/，导致根目录下面所有文件权限设定出了问题，额~重装系统吧，正好把装系统之后的配置过程记录下来。

这些都是我操作过的命令，确切可靠，适用于Ubuntu 10.10 Desktop Edtion。

    
    = init Linux programs and setting =
    :author: alswl
    :email: alswlx#gmail.com
    :toc:
    :numbered:

== first of all ==

.update (打补丁、升级)

----  
sudo apt-get update

Update System(fix bugs for sercurity): 299.0MB

----

.reset permission(谨慎使用，设定文件为644,设定文件夹为755)

----  
find /home/XXX -type d -exec chmod 755 {} ;

find /home/XXX -type f -exec chmod 644 {} ;

----

.nautilus (给鹦鹉螺加上open as administrator, open terminal)

----  
sudo apt-get install nautilus-open-terminal nautilus-gksu

----

.pdf (我使用Foxit)

----  
@see http://www.fuxinsoftware.com.cn/downloads/

----

== application ==

.fcitx (好用的中文输入法)

----  
sudo apt-get remove ibus

sudo add-apt-repository ppa:wengxt/fcitx-nightly

sudo apt-get update

sudo apt-get install fcitx fcitx-config-gtk fcitx-sunpinyin

im-switch -s fcitx -z default

----

.crebs(auto change desktop wallpaper)

----  
sudo add-apt-repository ppa:crebs/ppa

sudo apt-get update

sudo apt-get install crebs

----

.MÃ(C)tamorphose(rename tool)

----  
http://file-folder-ren.sourceforge.net/

----

== programing ==

.vim

----  
sudo apt-get install vim

sudo apt-get install vim-gnome

----

.jdk

----  
sudo add-apt-repository "deb http://archive.canonical.com/ubuntu maverick
partner"

sudo apt-get update

sudo apt-get install sun-java6-jre sun-java6-plugin sun-java6-source

sudo vi /etc/environment

CLASSPATH="/usr/lib/jvm/java-6-sun-1.6.0.24/lib"

JAVA_HOME="/usr/lib/jvm/java-6-sun-1.6.0.24"

sudo update-alternatives --config java

----

.eclipse

----  
@see http://blogold.chinaunix.net/u/21684/showart_367508.html

----

.idle(Python)

----  
sudo apt-get install idle

----

.lamp(安装过程中，使用Tab选定按钮来接受许可协议)

----  
sudo apt-get install apache2 php5-mysql libapache2-mod-php5 mysql-server

sudo apt-get install phpmyadmin

----

.maven

----  
sudo apt-get install maven2

----

.asciidoc(453MB)

----  
sudo apt-get install asciidoc

----

== media ==

.player

----  
sudo apt-get install smplayer

----

.gimp

----  
sudo apt-get install gimp

sudo apt-get install gimp-gap gimp-helpbrowser gimp-help-common gimp-help-zh-
cn gimp-manual libgimp-perl

----

.flash

----  
sudo apt-get install flashplugin-installer

----

.easytag(mp3 id3修改器)

----  
sudo apt-get install easytag exfalso

----

.picasa

----  
@see http://picasa.google.com/linux/

----

== net ==

.chrome

----  
sudo apt-get install chromium-browser

----

.firefox4

----  
sudo add-apt-repository ppa:mozillateam/firefox-stable

sudo apt-get update

sudo apt-get install firefox

---- 

另外，可以参见[Ubuntu cn wiki](http://wiki.ubuntu.org.cn/)里面的[Ubuntu 10.04
速配指南](http://wiki.ubuntu.org.cn/Qref/Lucid)。

最后，请大家使用sudo运行命令时候小心阿，别少了/或者~，惨痛教训呀。

