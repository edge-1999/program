# Centos

官网下载地址https://www.centos.org/download/

# 配置

## hosts

```shell
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
master 172.16.17.131
slave1 172.16.17.132
slave2 172.16.17.133
```

# ssh

重启虚拟机：`reboot -h now`

输入ip查询命名 `ip addr`

发现ens33 没有inet 这个属性，那么就没法通过IP地址连接虚拟机。

`vi /etc/sysconfig/network-scripts/ifcfg-ens33`

ONBOOT=no修改为ONBOOT=yes

然后重启网络服务： `sudo service network restart`

输入ip查询命名 `ip addr`

如果有就使用批量卸载命令`rpm -qa | grep java | xargs rpm -e --nodeps`

搜索jdk安装包：`yum search java|grep jdk`

# 查看版本

uname -a #查看内核版本等信息

uname -r

uname -m

cat /etc/issue 查看版本

cat /etc/redhat-release #查看centos版本

cat /proc/version

cat /proc/cpuinfo | grep "physical id" | uniq | wc -l #查看cpu个数

cat /proc/cpuinfo | grep "cpu cores" | uniq #查看cpu核数

cat /proc/cpuinfo | grep 'model name' |uniq #查看cpu型号

查看系统是32位或者64位的方法，getconf LONG_BIT or getconf WORD_BIT

输入：getconf LONG_BIT

file /bin/ls

# 环境变量

1、/root/.bashrc：全局变量、开机就会生效

2、/etc/profile：当用户登录之后生效

# 防火墙

修改完成防火墙需重启虚拟机

## 第一套防火墙

查看防火墙运行状态：`firewall-cmd --state`，返回信息running表示开启not running表示关闭

临时关闭防火墙：`systemctl stop firewalld.service`

永久关闭防火墙：`systemctl disable firewalld.service`会出现下面两句话

```shell
Removed symlink /etc/systemd/systemmulti-user.target.wants/firewalld.service.
Removed symlink /etc/systemd/system/dbus-org.fedoraproject.FirewallDi.service.
```

## 第二套防火墙SELinux

查看防火墙运行状态：`getenforce`，返回信息Enforcing表示运行，Permissive表示关闭

查看防火墙运行状态：`/usr/sbin/sestatus -v`

临时关闭防火墙：`setenforce 0`，防火墙关闭：Permissive

开启enforcing模式：`setenforce 1`

永久关闭防火墙：`vi /etc/selinux/config`修改SELINUX

```shell
SELINUX=enforcing
SELINUX=disabled#不适用arrch
SELINUX=permissive
```

如果输入错误会出现问题：进不去虚拟机、开不开机、开机报错

```shell
[FAILED] Failed to start Login Service.See
["systemct1 status systemd-logind,service'OK 1 Started D-Bus System Message Bus.for details.
```

出现此情况重启虚拟机然后在这个我不知道怎么进入的界面输入`init=/bin/bash`

```shell
fi
linux/umlinuz-5.11.12-300.e17.aarch64root=/dev/mapper/cl_fedora-root\
ro crashkernel=auto rd.lum.lu=cl_fedora/root rd.lum.lv=cl_fedora/swap rhgb qu\
it LANG-zh_CN.UTF-8
imitrd /initrans-5.11.12-300 .e17.aarch64. ima
```

```shell
fi
linux/umlinuz-5.11.12-300.e17.aarch64root=/dev/mapper/cl_fedora-root\
ro crashkernel=auto rd.lum.lu=cl_fedora/root rd.lum.lv=cl_fedora/swap rhgb qu\
it LANG-zh_CN.UTF-8  init=/bin/bash
imitrd /initrans-5.11.12-300 .e17.aarch64. ima
```

进入另外一个界面输入命令`mount -o rw,remount /`，接着再输入`vi /etc/selinux/config`，然后再次编辑，修改SELINUX值

```shell
SELINUX=enforcing
SELINUX=disabled#不适用Mac M1
SELINUX=permissive
```

# 静态IP

## VMware centos7 arrch M1

使用VMware vmnet8网络，先查看本地配置`cat /Library/Preferences/VMware\ Fusion/vmnet8/dhcpd.conf`

```shell
allow unknown-clients;
default-lease-time 1800;                # default is 30 minutes
max-lease-time 7200;                    # default is 2 hours

subnet 172.16.17.0 netmask 255.255.255.0 {#NETMASK=255.255.255.0
	range 172.16.17.128 172.16.17.254;#centos虚拟机区间IPADDR=172.16.17.136
	option broadcast-address 172.16.17.255;
	option domain-name-servers 172.16.17.2;#GATEWAY=172.16.17.2
	option domain-name localdomain;
	default-lease-time 1800;                # default is 30 minutes
	max-lease-time 7200;                    # default is 2 hours
	option netbios-name-servers 172.16.17.2;
	option routers 172.16.17.2;
}
host vmnet8 {
	hardware ethernet 00:50:56:C0:00:08;
	fixed-address 172.16.17.1;  # 本地inet 172.16.17.1
	option domain-name-servers 0.0.0.0;
	option domain-name "";
	option routers 0.0.0.0;
}
```

Mac M1输入`ifconfig|grep 17.1`。我目前返回信息如下

```shell
inet 172.16.17.1 netmask 0xffffff00 broadcast 172.16.17.255
```

`inet 172.16.17.1`就是局域网IP地址！Mac是 `192.168.1.100` 那么上面的 `CentOS` 就不能是这个地址了, 记住了哈, IP是唯一的, 就像你的身份证ID一样；`netmask 0xffffff00`这个是子网掩码, 它是用`16`进制表示的, 这可能与我们常常使用的Windows有些不一样, 并且还略显怪异, 我们都知道, IP地址是用 `32` 位表示的, 分为 `4` 段, 每段 `8` 位, 这 `8` 位呢！是 `0` 或 `1` 二进制组合来表示的, 那么转化为 `10` 进制, 它每段的取值就是 `0-255` 所示每段最小是 `0` 最大是 `255`, 这种表示方法在Windows上就是使用的 `10` 进制, 在 `Mac` 下如果存在最小 `0` 或 最大 `255` 它就会转化为 `16` 进制, 如果说当前的子网掩码是 `255.255.255.0`, 这是Windows下的 `10` 进制表示, 那到了 `Mac` 下 `Mac` 系统的研发工程师觉得老板发薪资了, 也不能闲着的时候没事干, 非得将 `10` 进制转换成 `16` 进制就成了我们现在看到的这个样子了 `0xffffff00`;`broadcast 172.16.17.255`这个呢是 `广播地址`, 主要的网络设备有 `路由器`、`防火墙`, `具有三层交换功能的网络交换机`及以 `通过软件开启了路由功能的主机`, 这个地址呢！可能会与IP不是一个网段, 这个要看局域网网络设备多少, 公司内部一般是不会跟IP地址网段一样, 还是那句话, 具体情况具体分析, 你可别较真哈, 像我在家里上网肯定就是一台无线路由器就搞定的事情, 那么这个 `广播地址`, 肯定是跟IP地址在一个网段, 最大 `10` 进制值表示这个 `广播地址` 也就是 `192.168.1.255`, 网卡中设置的是网关地址, 那么这个IP网段的第一个就是网关地址, 也就是 `192.168.1.1` 这个地址

Centos每台机器的ifcfg-ens XX都不一样，Centos查看网卡配置信息

`cat /etc/sysconfig/network-scripts/ifcfg-ens160`返回如下信息

```shell
TYPE=Ethernet# 网卡类型：为以太网
PROXY_METHOD=none# 代理方式：关闭状态
BROWSER_ONLY=no# 只是浏览器：否
BOOTPROTO=dhcp# 网卡的引导协议：DHCP[中文名称: 动态主机配置协议]
DEFROUTE=yes# 默认路由：是, 不明白的可以百度关键词 `默认路由`
IPV4_FAILURE_FATAL=no # 是不开启IPV4致命错误检测：否
IPV6INIT=yes# IPV6是否自动初始化: 是[不会有任何影响, 现在还没用到IPV6]
IPV6_AUTOCONF=yes# IPV6是否自动配置：是[不会有任何影响, 现在还没用到IPV6]
IPV6_DEFROUTE=yes# IPV6是否可以为默认路由：是[不会有任何影响, 现在还没用到IPV6]
IPV6_FAILURE_FATAL=no# 是不开启IPV6致命错误检测：否
#IPV6_ADDR_GEN_MODE=stable-privacy            # IPV6地址生成模型：stable-privacy [这只一种生成IPV6的策略]
NAME=ens160# 网卡物理设备名称
UUID=11b2adc2-7949-438c-a71b-17251ad90586# 通用唯一识别码, 每一个网卡都会有, 不能重复, 否两台linux只有一台网卡可用
DEVICE=ens160# 网卡设备名称, 必须和 `NAME` 值一样
ONBOOT=no # 是否开机启动， 要想网卡开机就启动或通过 `systemctl restart network`控制网卡,必须设置为 `yes`
```

编辑信息并插入如下`vi /etc/sysconfig/network-scripts/ifcfg-ens160` ，增加IPADDR、NETMASK、GATEWAY，修改BOOTPROTO、ONBOOT

```shell
#修改
BOOTPROTO=static#设置网卡引导协议为 静态
ONBOOT=yes#设置网卡启动方式为 开机启动 并且可以通过系统服务管理器 systemctl 控制网卡
#增加
IPADDR=172.16.17.136#IP
NETMASK=255.255.255.0#子网掩码
GATEWAY=172.16.17.2#网关地址
#不用添加
DNS1=127.207.160.106#首选DNS
DNS2=219.239.26.42#备用DNS
DNS1=8.8.8.8
DNS1=114.114.114.114  # 第1个DSN服务器的IP地址（重要）。
DNS2=1.2.4.8  # 第2个DSN服务器的IP地址（重要）。
```

如下信息可删除

```shell
IPV4_FAILURE_FATAL=no # 是不开启IPV4致命错误检测：否
IPV6INIT=yes# IPV6是否自动初始化: 是[不会有任何影响, 现在还没用到IPV6]
IPV6_AUTOCONF=yes# IPV6是否自动配置：是[不会有任何影响, 现在还没用到IPV6]
IPV6_DEFROUTE=yes# IPV6是否可以为默认路由：是[不会有任何影响, 现在还没用到IPV6]
IPV6_FAILURE_FATAL=no# 是不开启IPV6致命错误检测：否
#IPV6_ADDR_GEN_MODE=stable-privacy            # IPV6地址生成模型：stable-privacy [这只一种生成IPV6的策略]
```

上面是最主要的3个配置项[IP/子网掩码/网关], 配置完成这些参数先保存退出,

重启网卡:`systemctl restart network`或`service network restart`，说明一点, 在 CentOS7 下已全面使用 `systemctl` 作为服务管理器, 它用来替代 `service 和 chkconfig`, 现在 `RadHat`、`Ubuntu`、`fedora` 等主流的 `linux` 发行版本都以全面支持 `systemctl` 服务管理器。

配置以上网卡信息后当前网卡状态:`ip addr`

测试能不能访问外网`ping www.baidu.com`，大概率是不能，需去`vi /etc/resolv.conf`修改

```shell
#主DNS服务器
nameserver 223.5.5.5
#备DNS服务器
nameserver 223.6.6.6
```

测试能不能访问外网`ping www.baidu.com`大概率可

# wget

`wget -V`

`yum install wget -y`

# net-tools

`net-tools` 工具包, 包含以下命令：arp, hostname, ifconfig, ipmaddr, iptunnel, mii-tool, nameif, netstat, plipconfig, rarp, route und slattach. 关于 `net-tools` 更多的详情信息请参考: [https://net-tools.sourceforge.io/](https://net-tools.sourceforge.io/)

`ifconfig`报错-bash: ifconfig: 未找到命令

那么你可能使用通过 `yum` 软件包管理工具进行安装：`yum install -y ifconfig`很不幸你会得到这么一个结果没有可用软件包 **ifconfig**。那这个时候你就要通过:`yum whatprovides package_name`来查找包名了, 如现在要查找 `ifconfig` 这个命令, 具体包含在哪个包里就可以这么做:`yum whatprovides ifconfig`，在这里有可能会成功，可能会看到这样的结果,  原因是CentOS在 `yum` 源在国内使用非常不稳定, 建议更新为国内的 `yum` 源, 比如 `阿里` 或是 `网易`

```other
yum whatprovides ifconfig
yum install -y net-tools
```

# 文件

## 上传文件

Linux：`yum -y install lrzsz`

移动文件：`mv 文件名 文件名 … 路径（相对路径和绝对路径）`

解压文件：`tar -zxvf 文件名`

# yum

## 更新yum源

更新 `CentOS7` 默认 `yum` 源, 需要以下几个步骤:备份当前系统默认 `yum` 源配置文件

`mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak`

- 查看当前 `CentOS7` 版本号`cat /etc/centos-release`

到阿里云开源镜像站找到对应的 `yum` 源版本，详情参考: [阿里yum源](https://link.segmentfault.com/?enc=9dP7xDZlUDdIPyenZeVuTg%3D%3D.HbsQEojOGJcjAIif4nedwEXucTVi6btYAUo1mf7Su4EeYwh6NezcNB%2BPWa1CCfp5) [网易yum源](https://link.segmentfault.com/?enc=twaxmEIPFCShTBiNHRxkzQ%3D%3D.mF5JVPDi4i73zHs2yWhfoF%2Fot8XDCWsZjHGtkwR%2BhHDsX8%2B69iFyuz%2BSBt7V7z5T)

`wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo`

yum -y install vim*

# 时间同步

yum install -y ntp

ntpdate -u [ntp.api.bz](http://ntp.api.bz)

# 远程服务器

安装samba服务器：`yum install samba`

设置共享文件夹：打开smb配置文件`vim /etc/samba/smb.conf`，在文件末尾添加共享文件夹。

```shell
# See smb.conf.example for a more detailed config file or
# read the smb.conf manpage.
# Run 'testparm' to verify the config is correct after
# you modified it.
[global]
 workgroup = SAMBA #samba的工作组，设置成 Windows 的工作组
 netbios name = zkserver  # <==主机名称，跟hostname不是一个概念，在同一个组中，netbios name必须唯一

 printing = cups
 printcap name = cups
 cups options = raw
 
 #与登录文件有关的设置
  log file = /var/log/samba/log.%m   <==日志文件的存储文件名，%m代表的是client端Internet主机名，就是hostname
   max log size = 50      <==日志文件最大的大小为50Kb
  #与密码相关的设置
  # security = share       <==表示不需要密码，可设置的值为share、user和server
  security = user  #安全选项，可以是 share|user|server|domain，安全级别递增
  passdb backend = tdbsam
  #打印机加载方式   load printer = no <==不加载打印机
  load printers = yes
 
[homes] # 共享默认会将用户的主目录共享 , 这是不安全的 , 可以将其注释
 comment = Home Directories
 valid users = %S, %D%w%S
 browseable = No
 read only = No
 inherit acls = Yes
[printers] #打印机共享
 comment = All Printers
 path = /var/tmp
 printable = Yes
 create mask = 0600
 browseable = No
[print$]
 comment = Printer Drivers
 path = /var/lib/samba/drivers
 write list = root
 create mask = 0664
 directory mask = 0775

[rootdir] #自定义的共享文件夹
 comment = SambaRoot
 path = /home/samba/ #共享的路径
 read only = No
$ [centos_share_folder]
      comment = share folder#共享文件夹
      path = /home/centos/share#指定共享文件夹路径
      available = yes
      public = yes
      writable = yes  # 设置为可写入
      valid users = centos
      create mask = 755
      directory mask = 755
      guest ok = no
      browseable = yes   # <==可以被所有用户浏览到资源名称，
      guest ok = yes    # <==可以让用户随意登录
```

然后wq保存退出。

添加用户

`adduser centos`

`smbpasswd -a root`

`123456`

```other
adduser centos
smbpasswd -a samba

adduser centos
smbpasswd -a samba

useradd samba
smbpasswd -a samba

groupadd liugroup #这里的liugroup是用户所在的组
smbpasswd -a root  # 添加用户

// 添加 Samba 用户帐号
# smbpasswd -a sambauser 
// 禁用 Samba 用户帐号
# smbpasswd -d sambauser
// 启用 Samba 用户帐号
# smbpasswd -e sambauser
// 删除 Samba 用户帐号
# smbpasswd -x sambauser
```

重启smb，并设置开机启动

```javascript
service smb restart
systemctl enable smb.service
systemctl enable nmb.service
```

```javascript
systemctl start smb  # 启动
systemctl stop smb  # 停止、
systemctl status smb  # 查看相关命令
```

开启samba服务

```javascript
$ systemctl start smb.service
$ systemctl stop smb.service
$ systemctl restart smb.service
```

查看smb状态：

```javascript
systemctl status smb
```

