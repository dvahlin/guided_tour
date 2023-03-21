FROM fedora:latest

RUN yum update -y && yum install tmux util-linux ncurses binutils psmisc procps strace python3-pip util-linux -y
RUN pip3 install --no-cache-dir alive-progress
RUN useradd -ms /bin/bash ctf

COPY HELP.txt /home/ctf/HELP.txt
COPY JvA-0170046159 /home/ctf/
COPY JvA-5340667988 /home/ctf/work/.JvA-5340667988
COPY work /home/ctf/work
COPY ctf.py /home/ctf/ctf.py
COPY challenge.json /home/ctf/challenge.json
COPY bashrc /home/ctf/.bashrc
COPY tmux.conf /home/ctf/.tmux.conf
RUN chown -R ctf:ctf /home/ctf/work
USER ctf
#CMD ["tmux", "capture-pane", "-b", "temp-capture-buffer", "-S -"]
#CMD ["tmux", "capture-pane", "-pS", "-3000", "-t2", ">", "/var/tmp/ctfrd"]
#CMD ["tmux", "attach"]
#CMD ["su", "-", "ctf", "-c", "/bin/bash"]
COPY ./entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
