#/usr/bin/env python
#coding=uth8
#######################
# install python
#1.选择python版本
#2.下载python源码
#3.解压源码
#4.编译与安装

import os.sys

if os.getuid() == 0:
	pass
else:
	print ('请以root用户执行脚本')
	sys.exit(1)

version = raw_input('请输入你想安装的python版本(2.7/3.5)')
if version == '2.7':
    url = "https://www.python.org/ftp/python/2.7.16/Python-2.7.16.tgz"
elif version == '3.5':
	url = "https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz"
else:
	print ('输入的版本号有误，请输入2.7或3.5')
	sys.exit(1)

cmd = 'wget ' +url
res = os.system(cmd)
if res != 0:
	print('下载源码包失败，请检查网络')
	sys.exit(1)

if version == '2.7':
	package_name = 'Python-2.7.12'
else:
	package_name = 'Python-3.5.2'
cmd = 'tar xf '+package_name+'.tgz'
res = os.system(cmd)
if res != 0:
	os.system('rm '+package_name+'.tgz')
	print('解压源码包失败，请重新运行脚本下载源码包')
	sys.exit(1)

cmd = 'cd '+package_name+' && ./configure --prefix=/usr/local/python && make && make install'
res = os.system(cmd)
if res != 0:
	print('编译python源码失败，请检查是否缺少依赖库')
	sys.exit(1)

#dependency = "yum groupinstall -y 'Development Tools' && yum install -y zlib-devel bzip2-devel openssl-devel readline-devel libffi-devel"