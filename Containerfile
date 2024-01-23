FROM fedora:latest

RUN yum update -y && \
    yum groupinstall -y "Development Tools" && \
    yum install -y tmux util-linux ncurses binutils psmisc procps strace python3-pip util-linux nodejs gcc-c++ make

# Install pip3 packages
RUN pip3 install --no-cache-dir alive-progress


# Add user
RUN useradd -ms /bin/bash ctf

# Create a directory for the app
RUN mkdir -p /home/ctf/app && chown -R ctf:ctf /home/ctf/app
WORKDIR /home/ctf/app

# Install Node.js deps
COPY package.json ./
RUN npm install

# Copy app
COPY web-terminal-server.js ./
COPY public /var/www/public

# Copy CTF/script
COPY HELP.txt /home/ctf/HELP.txt
COPY JvA-0170046159 /home/ctf/
COPY JvA-5340667988 /home/ctf/work/.JvA-5340667988
COPY work /home/ctf/work
COPY ctf.py /home/ctf/ctf.py
COPY challenge.json /home/ctf/challenge.json
COPY bashrc /home/ctf/.bashrc
COPY tmux.conf /home/ctf/.tmux.conf

#Permissions
RUN chown -R ctf:ctf /home/ctf/work

# Exose Web
EXPOSE 3000

# Set entrypoint
USER ctf
#CMD ["tmux", "capture-pane", "-b", "temp-capture-buffer", "-S -"]
#CMD ["tmux", "capture-pane", "-pS", "-3000", "-t2", ">", "/var/tmp/ctfrd"]
#CMD ["tmux", "attach"]
#CMD ["su", "-", "ctf", "-c", "/bin/bash"]
COPY ./entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
