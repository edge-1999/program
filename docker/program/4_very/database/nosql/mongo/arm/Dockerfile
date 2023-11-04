FROM --platform=linux/arm64/v8 mongo:latest
LABEL authors="li"

# 设置环境变量，这些都是可以按需调整的
ENV MONGO_INITDB_ROOT_USERNAME=root
ENV MONGO_INITDB_ROOT_PASSWORD=li19990929..

# 创建数据目录和配置目录
RUN mkdir -p /data/db /data/configdb

# 将宿主机上的数据目录和配置目录映射到容器内
#VOLUME ["/data/db", "/data/configdb"]

# Expose the default MongoDB port
EXPOSE 27017

# Run the main MongoDB process
CMD ["mongod"]
