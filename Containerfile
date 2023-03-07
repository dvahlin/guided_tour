FROM fedora:latest

RUN yum update -y && yum install tmux util-linux ncurses binutils psmisc python3-pip -y
RUN pip3 install --no-cache-dir alive-progress
RUN useradd -ms /bin/bash ctf

COPY HELP.txt /home/ctf/HELP.txt
COPY work /home/ctf/work
COPY ctf.py /home/ctf/ctf.py
COPY challenge.json /home/ctf/challenge.json
COPY bashrc /home/ctf/.bashrc
COPY tmux.conf /home/ctf/.tmux.conf
RUN chown -R ctf:ctf /home/ctf/work
USER ctf
CMD ["tmux", "attach"]
#CMD ["su", "-", "ctf", "-c", "/bin/bash"]
