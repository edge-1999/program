FROM mongo:4.4
LABEL authors="li"

# 设置环境变量，这些都是可以按需调整的
ENV MONGO_INITDB_ROOT_USERNAME=root
ENV MONGO_INITDB_ROOT_PASSWORD=li19990929..

# 将自己的配置文件复制到容器中
# COPY mongo.conf /etc/mongo/mongo.conf
# 请注意，如果你有自定义的mongo.conf，需要取消上面的注释并提供该文件

# 设置数据目录和配置文件的权限
#RUN chown -R mongodb:mongodb /var/lib/mongodb
#RUN chown mongodb:mongodb /etc/mongo/mongo.conf

#WORKDIR /usr/src/mongo

# 暴露MongoDB默认端口
EXPOSE 27017

# 使用默认的CMD启动MongoDB
CMD ["mongod"]

#VOLUME ["/data/db", "/data/configdb", "/var/log/mongodb", "/etc/mongod.conf", "/backup"]
