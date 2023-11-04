FROM --platform=linux/arm64/v8 golang:latest AS builder
LABEL authors="li"

# 设置工作目录
WORKDIR /program

# 复制 go.mod 和 go.sum 文件
COPY go.mod go.sum ./

# 下载依赖
RUN go mod download

# 复制源代码到容器内
COPY . .

# 构建应用
RUN go build -o myapp

# 使用 alpine 镜像作为运行环境
FROM alpine:latest

# 在新的镜像中设置工作目录
WORKDIR /program/

# 从构建器镜像中复制构建的二进制文件到当前目录
COPY --from=builder /program .

# 运行应用
CMD ["./myapp"]
