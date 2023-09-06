#export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.ustc.edu.cn/brew.git"
#export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git"
#export HOMEBREW_BOTTLE_DOMAIN="https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles"
#export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git"
# >>> set libarchive environment >>>
export GUILE_TLS_CERTIFICATE_DIRECTORY=/opt/homebrew/etc/gnutls/
export PATH="/opt/homebrew/opt/libarchive/bin:$PATH"
export PATH="/opt/homebrew/opt/icu4c/sbin:$PATH"
export LDFLAGS="-L/opt/homebrew/opt/libarchive/lib"
export CPPFLAGS="-I/opt/homebrew/opt/libarchive/include"
# <<< end libarchive environment <<<

# >>> set binutils environment >>>
export PATH="/opt/homebrew/opt/binutils/bin:$PATH"
#export LDFLAGS="-L/opt/homebrew/opt/binutils/lib"
#export CPPFLAGS="-I/opt/homebrew/opt/binutils/include"
# <<< end binutils environment <<<

export GUILE_TLS_CERTIFICATE_DIRECTORY="/opt/homebrew/etc/gnutls/"

# >>> set tesseract environment >>>
export TESSDATA_PREFIX=/Users/li/Drive/Mac/Tool/Brew/tesseract/tessdata
# <<< end tesseract environment <<<

# >>> set openjdk environment >>>
# sudo ln -sfn /opt/homebrew/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk
#echo 'export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"' >> ~/.zshrc
export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"
export CPPFLAGS="-I/opt/homebrew/opt/openjdk/include"
#export TESSDATA_PREFIX=""
# <<< end openjdk environment <<<
