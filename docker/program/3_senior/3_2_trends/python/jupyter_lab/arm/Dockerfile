FROM jupyter/base-notebook:latest

USER root
RUN echo 'root:li19990929..' | chpasswd
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    libzmq3-dev \
    vim \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 安装软件属性包以便后续可以添加 PPA
RUN apt-get update && apt-get install -y software-properties-common

# 添加死守Python PPA
RUN add-apt-repository ppa:deadsnakes/ppa

# 安装Python 3.9
RUN apt-get update && apt-get install -y python3.12 python3.12-venv python3.12-dev

# 更新默认的python命令到新版本
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.12 1

RUN conda install --quiet --yes \
    'jupyterlab' \
    'notebook' \
    'pandas' \
    'numexpr' \
    'matplotlib' \
    'scipy' \
    'seaborn' \
    'scikit-learn' \
    'scikit-image' \
    'sympy' \
    'cython' \
    'patsy' \
    'statsmodels' \
    'cloudpickle' \
    'dill' \
    'numba' \
    'bokeh' \
    'sqlalchemy' \
    'hdf5' \
    'h5py' \
    'vincent' \
    'beautifulsoup4' \
    'protobuf' \
    'xlrd' \
    && conda clean --all -f -y

RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager

WORKDIR /program

# 设置Jupyter配置文件的位置
ENV JUPYTER_CONFIG_DIR /program/env/docker/program/3_senior/3_2_trends/python/jupyter_lab.arm

#COPY requirements.txt ./
#RUN pip install -r requirements.txt -i https://pypi.douban.com/simple
#RUN rm ./requirements.txt

#COPY ./start.sh /usr/local/bin/start.sh
#RUN chmod +x /usr/local/bin/start.sh
#CMD ["/usr/local/bin/start.sh"]

EXPOSE 22
EXPOSE 8888

USER $NB_UID

#CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
CMD ["start.sh", "jupyter", "lab", "--ip=0.0.0.0", "--allow-root"]
