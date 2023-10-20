# Ubuntu

# 安装

## Docker

搜索镜像：`docker search ubuntu`

拉取镜像：`docker pull ubuntu`

检查镜像：`docker images`

创建容器：`docker run -itd --name linux -p80:80 --privileged ubuntu:latest` （docker run -itd --name linux -p80:80 --privileged ubuntu:latest /usr/sbin/init、docker run -itd --name linux -p 80:80 -p 7070:7070 --privileged ubuntu:latest /usr/sbin/init）

进入容器：`docker exec -it linux bash`（docker exec -it 镜像ID /bin/bash 或者 docker exec -it 镜像名称 bash）

# 配置

先更新：`apt-get update`、`apt-get upgrade`

下载net-tools：`apt-get install net-tools`（可能会需要权限）

apt-get install curl

apt-get install build-essential

```other
apt-get install mlocate
```

```other
apt-get install openssh-server
```

SSH

/etc/init.d/ssh start

- 查看用户名`whoami`
- 查看ip地址`ifconfig`（注意箭头所指的就是我们要用的ip地址）

