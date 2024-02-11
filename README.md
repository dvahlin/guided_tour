# guided_tour
Mini framework for education

# Starting

```
Build:
podman build -t "linux-ctf-container" .
Run:
podman run -p 3000:3000 linux-ctf-container
```


GLHF



## Development
```
podman run --rm -it -e COLUMNS="$(tput cols)" -e LINES="$(tput lines)" --name linux-ctf -d -it linux-ctf-container:latest 
podman exec -it --user ctf linux-ctf /bin/bash
```

# Todo... 
- adjust for autocompletion on tasks
