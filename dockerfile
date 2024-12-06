FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y openssh-server python3 sudo && \
    apt-get clean

RUN mkdir /var/run/sshd
RUN echo 'root:password' | chpasswd

RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

RUN mkdir -p /root/.ssh && chmod 700 /root/.ssh

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
