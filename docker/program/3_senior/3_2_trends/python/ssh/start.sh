#!/bin/bash

# 增加文件描述符
#ulimit -n 1024

# 启动 SSH 服务（作为后台进程）
sudo service ssh start

# 使用官方脚本启动 Jupyter Notebook（作为前台进程）
exec start-notebook.py --NotebookApp.notebook_dir=/program
