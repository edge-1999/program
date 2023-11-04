#FROM --platform=linux/arm64/v8 mysql:8.0
FROM mysql:oracle
LABEL authors="li"

RUN mkdir -p /var/lib/mysql \
            /var/log/mysql \
            /etc/mysql/conf.d \
            /docker-entrypoint-initdb.d \
            /etc/mysql/certificates \
            /var/backups/mysql

ENV MYSQL_ROOT_PASSWORD=li19990929..
# ENV MYSQL_DATABASE=mydatabase

# 数据存储目录
VOLUME /var/lib/mysql

# 配置文件目录
VOLUME /etc/mysql

# 日志文件目录
VOLUME /var/log/mysql

# 其他相关目录
VOLUME /etc/mysql/conf.d
VOLUME /etc/mysql/mysql.conf.d
VOLUME /var/lib/mysql-files
VOLUME /var/lib/mysql-keyring
VOLUME /var/run/mysqld
VOLUME /var/log/mysql/error.log

EXPOSE 3306

CMD ["mysqld"]
