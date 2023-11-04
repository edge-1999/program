FROM jupyter/scipy-notebook:latest
LABEL authors="li"

USER root

# 增加文件描述符
#RUN ulimit -n 1024

# 设置Jupyter配置文件的位置
ENV JUPYTER_CONFIG_DIR /etc/jupyter
WORKDIR /program

EXPOSE 22
EXPOSE 8888

RUN apt-get update && apt-get install -y openssh-server && \
    mkdir /var/run/sshd && \
    echo 'root:li19990929..' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN echo "jovyan:li19990929.." | chpasswd

COPY ./start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh

CMD ["/usr/local/bin/start.sh"]
