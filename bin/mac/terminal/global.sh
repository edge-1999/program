function proxy_on() {
  #  export http_proxy=http://127.0.0.1:1087;export https_proxy=http://127.0.0.1:1087;
  #  export http_proxy=http://127.0.0.1:1087
  #  export https_proxy=http://127.0.0.1:1087
  #  export ALL_PROXY=socks5://127.0.0.1:1086
  # set clashX environment
  #  export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890
  export https_proxy=http://127.0.0.1:7890
  export http_proxy=http://127.0.0.1:7890
  export all_proxy=socks5://127.0.0.1:7890
}
function proxy_off() {
  unset ALL_PROXY
  unset http_proxy
  unset https_proxy
  echo -e "已关闭代理"
}
# set ss environment
#export http_proxy=127.0.0.1:59263
#export https_proxy=127.0.0.1:59263
#export ftp_proxy=127.0.0.1:59263
#export http_proxy=http://localhost:59263
#export https_proxy=http://localhost:59263
#export ftp_proxy=127.0.0.1:59263
# set VPN V2ray environment
#export http_proxy=http://127.0.0.1:1087
#export https_proxy=http://127.0.0.1:1087
#export ALL_PROXY=socks5://127.0.0.1:1086
