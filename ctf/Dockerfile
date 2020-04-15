# Build image
# docker image build -t kali .

# Run image and get shell
# Windows
# docker run -v ${pwd}:/ctf -ti kali
# Linux
# docker run -v $(pwd):/ctf -ti kali

FROM kalilinux/kali

ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm-256color

# Set up the basics
WORKDIR /root/

#COPY files/* files/
#COPY exploit.sh .

# Kali basic tool install
RUN apt-get clean
RUN apt-get update -y
RUN apt-get install -y software-properties-common kali-linux-full --fix-missing
RUN apt-get install -y \
# Basic
  git \
  colordiff \
  colortail \
  vim \
  tmux \
  xterm \
  less \
  bash-completion \
  build-essential \
  python3-setuptools \
  python3-pip \
  tor \
  proxychains \
  unzip \
  p7zip-full \
# Network
  curl \
  wget \
  nmap \
  netcat \
  telnet \
  net-tools \
  iputils-tracepath \
  iputils-ping \
  whois \
# Web hacking
  enum4linux \
  hydra \
  gobuster \
# Exploit
  strace \
  ltrace \
  tmate \
  proxychains4 \
  zstd \
  bsdmainutils \
  exif \
  vsftpd \
# Cracking
  john --fix-missing

# Setting up ssh
RUN apt-get install -y openssh-server

RUN service ssh start

# Python modiles
RUN pip3 install olefile

# Wordlists
# https://gitlab.com/kalilinux/packages/wordlists
RUN git clone https://gitlab.com/kalilinux/packages/wordlists.git /usr/share/wordlists/
RUN gzip -d /usr/share/wordlists/rockyou.txt.gz
RUN mkdir /usr/share/wordlists/dirb
RUN curl https://raw.githubusercontent.com/v0re/dirb/master/wordlists/common.txt -o /usr/share/wordlists/dirb/common.txt

# Malware analysis tool
RUN git clone https://github.com/DidierStevens/DidierStevensSuite.git oledump

# Privilege escalation tools
#RUN curl https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh -o linenum.sh
RUN curl https://raw.githubusercontent.com/carlospolop/privilege-escalation-awesome-scripts-suite/master/linPEAS/linpeas.sh -o linpeas.sh

EXPOSE 8080 80 443 21

# Post commands

#RUN echo "sed \"s/#PermitRootLogin prohibit-password/PermitRootLogin yes/g\" /etc/ssh/sshd_config"
