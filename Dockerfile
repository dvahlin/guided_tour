FROM fedora:latest

RUN yum update -y
RUN yum install tmux -y
RUN yum install util-linux -y
RUN yum install ncurses -y
RUN yum install binutils -y
RUN yum install python3-pip -y
RUN pip3 install --no-cache-dir alive-progress

RUN useradd -ms /bin/bash ctf

COPY HELP.txt /home/ctf/HELP.txt
COPY work /home/ctf/work
COPY ctf.py /home/ctf/ctf.py
COPY bashrc /home/ctf/.bashrc
COPY tmux.conf /home/ctf/.tmux.conf
RUN chown -R ctf:ctf /home/ctf/work
#RUN su ctf
#CMD ["su", "-", "ctf", "-c", "tmux attach -d"]
#CMD ["su", "-", "ctf", "-c", "/bin/bash"]
