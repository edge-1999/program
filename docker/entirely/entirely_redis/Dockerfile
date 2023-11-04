FROM redis:latest
LABEL authors="li"

# 设置工作目录
WORKDIR /data
# 创建并定义数据和配置的共享目录
VOLUME /data
VOLUME /usr/local/etc/redis/

# 启动Redis服务器并使用自定义配置
CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]

EXPOSE 6379
