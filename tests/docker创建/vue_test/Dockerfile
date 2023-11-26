FROM --platform=linux/arm64/v8 node:latest

# 设置工作目录
WORKDIR /usr/src/app

# 复制 package.json 和package-lock.json文件,这俩是什么意思？并且给我一个案例
#COPY package*.json ./
#COPY package-lock.json ./

# 复制项目文件到工作目录
COPY . .

# 安装项目依赖
RUN npm install

# 暴露容器运行时的端口
EXPOSE 3000

# 容器启动时运行的命令
CMD ["node", "app.js"]