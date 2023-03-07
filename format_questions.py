import json
import os

challenges = [
    {
        "question": "List the content in this folder",
        "command" : "ls", 
        "hint" : "LiSt"
    },
    {
        "question": "Change into work",
        "command": ["cd work", "cd work/"], 
        "hint": "Change Directory",
    },
    {
        "question": "Print current working directory",
        "command": "pwd",
        "hint": "Print Working Directory",
    },
    {
        "question": "Print the content of random.txt",
        "command": "cat random.txt",
        "hint": "enemy of dogs",
    },
    {
        "question": "Delete the random.txt file",
        "command": "rm random.txt",
        "hint": "ReMove",
    },
    {
        "question": "I think there is a hidden copy, find it",
        "command" : "ls -la", 
        "hint" : "LiSt with flags"
    },

]

with open("challenge.json","w") as f:
    json.dump(challenges,f)
