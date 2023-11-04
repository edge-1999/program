FROM jupyter/scipy-notebook:latest
#FROM jupyter/base-notebook:latest
LABEL authors="li"

# 设置工作目录
WORKDIR /program

# (可选) 安装其他你需要的Python库
#RUN pip install numpy pandas matplotlib

# 设置Jupyter配置文件的位置
ENV JUPYTER_CONFIG_DIR /etc/jupyter

EXPOSE 8888

# 将默认启动目录设置为 /program
CMD ["start-notebook.sh", "--NotebookApp.notebook_dir=/program"]
