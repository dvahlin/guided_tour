import json
import os

challenges = [
    {
        "question": "You will now test your linux-fu!",
        "command" : "ls", 
        "hint" : "LiSt"
    },
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
    {
        "question": "Make a copy of the hidden file in the current folder, name it random.txt",
        "command": "cp .hidden_random.txt random.txt",
        "hint": "CoPy?",
    },
    {
        "question": "Make flagme executable",
        "command": "chmod +x flagme",
        "hint": "man chmod",
    },
    {
        "question": "Run flagme and decode the message and run echo flag{value}",
        "command": "echo \"flag{encoded_or_decoded_not_encrypted}\"",
        "hint": "execute me ./now, and is that the base?",
    },
    {
        "question": "Find the hidden FLAG in in_plain_sight and run echo flag{value} ",
        "command": "echo \"flag{strings_pipe_grep?}\"",
        "hint": "grep for it!",
    },

]

with open("challenge.json","w") as f:
    json.dump(challenges,f)
