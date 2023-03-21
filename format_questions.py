import json
import os

challenges = [
    {
        "question": "List the content in this folder",
        "flag" : "JvA-0170046159", 
        "hint" : "LiSt"
    },
    {
        "question": "Change into work",
        "flag": ["work"], 
        "hint": "Change Directory",
    },
    {
        "question": "Print current working directory",
        "flag": "/home/ctf/work",
        "hint": "Print Working Directory",
    },
    {
        "question": "Print the content of random.txt",
        "flag": "JvA-1053732816",
        "hint": "enemy of dogs",
    },
    {
        "question": "Delete the random.txt file",
        "flag": "rm random.txt",
        "hint": "ReMove",
    },
    {
        "question": "I think there is a hidden copy, find it",
        "flag" : "JvA-5340667988", 
        "hint" : "LiSt with flags"
    },

]

with open("challenge.json","w") as f:
    json.dump(challenges,f)
