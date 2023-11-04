FROM jupyter/scipy-notebook:latest
#FROM jupyter/base-notebook:latest
LABEL authors="li"

# Install SSH server
USER root
# 切换回 jovyan 用户
# USER $NB_UID
RUN apt-get update && apt-get install -y openssh-server && \
    mkdir /var/run/sshd && \
    echo 'root:li19990929..' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN echo "jovyan:li19990929.." | chpasswd

WORKDIR /program
COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.douban.com/simple
RUN rm ./requirements.txt

EXPOSE 22
EXPOSE 8888

# 设置Jupyter配置文件的位置
ENV JUPYTER_CONFIG_DIR /etc/jupyter

# 将默认启动目录设置为 /program
# CMD ["start-notebook.sh", "--NotebookApp.notebook_dir=/program"]

# /program/3_senior/3_2_trends/python/start.sh
COPY /Users/Shared/program/assets/docker/program/3_senior/3_2_trends/python/start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh
#ENTRYPOINT ["/usr/local/bin/start.sh"]

# 设置容器启动时执行的命令
CMD ["/usr/local/bin/start.sh"]
