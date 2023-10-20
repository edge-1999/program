# Linux

# 基础命令

查看系统信息：`lsb_release -a`

查看位数：`uname -a`

`cat /proc/version`

更新源：`sudo apt-get update`

----

# 错误

W: GPG 错误：[http://dl.google.com/linux/chrome/deb](http://dl.google.com/linux/chrome/deb) stable InRelease: 由于没有公钥，无法验证下列签名： NO_PUBKEY 78BD65473CB3BD13 E: 仓库 “[http://dl.google.com/linux/chrome/deb](http://dl.google.com/linux/chrome/deb) stable InRelease” 的签名不再生效。 N: 无法安全地用该源进行更新，所以默认禁用该源。 N: 参见 apt-secure(8) 手册以了解仓库创建和用户配置方面的细节。 3CB3BD13

# 解决方案

#### 方案1

`gpg --keyserver` [`wwwkeys.pgp.net`](http://wwwkeys.pgp.net)` --recv-keys 209088E7 # gpg --armor --export 209088E7 | apt-key add`

`gpg --keyserver` [`wwwkeys.pgp.net`](http://wwwkeys.pgp.net)` --recv-keys 3CB3BD13`

`gpg --armor --export 3CB3BD13 | apt-key add -`

#### 方案2

`gpg --keyserver` [`wwwkeys.pgp.net`](http://wwwkeys.pgp.net)` --recv-keys 3CB3BD13 # gpg --armor --export 209088E7 | apt-key add -`

----

sudo rm -r -f

rm -rf

uname -a #查看内核版本等信息

uname -r

uname -m

scp -rp [archiconda3-0.2.3-linux-aarch64.sh](http://archiconda3-0.2.3-linux-aarch64.sh) [root@172.16.17.132](mailto:root@172.16.17.132):~

# net-tools

# wget

yum install -y wget

#### CURL

sudo apt-get update

apt-get install curl

sudo apt-get update

