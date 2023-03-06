# guided_tour
Mini framework for education


Build:
podman build -t "linux-ctf-container" .
Run:
podman run --rm -it -e COLUMNS="$(tput cols)" -e LINES="$(tput lines)" --name linux-ctf -d -it linux-ctf-container:latest 
Enter:
podman exec -it --user ctf linux-ctf /bin/bash
Quit:
podman container stop linux-ctf

# in container RUN... 
su ctf
tmux attach 

GLHF


# Todo... 
- make tmux attach when entering container with kept variables
- adjust for autocompletion on tasks
- Add killevent when "finished"
