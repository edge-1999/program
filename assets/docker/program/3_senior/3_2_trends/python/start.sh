#!/bin/bash

# 启动 SSH 服务（作为后台进程）
sudo service ssh start

# 使用官方脚本启动 Jupyter Notebook（作为前台进程）
exec start-notebook.sh --NotebookApp.notebook_dir=/program
