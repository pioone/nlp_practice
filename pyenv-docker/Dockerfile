# docker build -t my-python-app .
# pyenvでpythonのバージョン管理を行い、開発環境を作成する

FROM ubuntu:latest

# "tzdata"をこの時点でインストールしている
RUN apt-get update && \
    apt-get install -y software-properties-common \
                       tzdata

RUN apt-add-repository -y ppa:git-core/ppa && \
    apt-get update && \
    apt-get install -y git \
                       vim

RUN git clone https://github.com/pyenv/pyenv.git ~/.pyenv
RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc && \
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc

RUN echo 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc

RUN apt-get install -y make build-essential libssl-dev zlib1g-dev \
                       libbz2-dev libreadline-dev libsqlite3-dev wget \
                       curl llvm libncurses5-dev xz-utils tk-dev \
                       libxml2-dev libxmlsec1-dev libffi-dev nkf

ENV PATH $PATH:/root/.pyenv/bin

RUN pyenv install 3.6.7 && \
    pyenv global 3.6.7 && \
    pyenv rehash

ENV PATH $PATH:/root/.pyenv/shims

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
