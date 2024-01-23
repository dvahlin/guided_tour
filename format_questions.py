import json
import os
import base64

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
    {
        "question": "Fix the program \"motivation\" so it can run on the system, then run the program",
        "flag" : "Ready Player One", 
        "hint" : "chmod"
    },
    {
        "question": "There might be more to this program, can you find the hidden flag?",
        "flag" : "JvA-1478754256", 
        "hint" : "strings"
    },
    {
        "question": "In the folder maze there are several files.. how many in total?",
        "flag" : "99", 
        "hint" : "find/ls | wc -l"
    },
    {
        "question": "In the folder maze there are several files.. how many are larger than 250 bytes?",
        "flag" : "85", 
        "hint" : "find | wc -l"
    },
    {
        "question": "In the folder maze there is a file that is larger than 241 bytes but smaller than 245 bytes. To proceed you need to print it backwards on the terminal",
        "flag" : "txt.l6aPZGXIxU", 
        "hint" : "find size"
    },
    {
        "question": "In the folder work/data you will find a file called people.csv. Check so the md5sum is correct cc87d3e47907e63d40ddb702b338b7fe",
        "flag" : "cc87d3e47907e63d40ddb702b338b7fe", 
        "hint" : "md5sum"
    },
    {
        "question": "How many people live in San Francisco? feel free to use the tool of your choosing, but for coming adventures AWK might be a good thing to start with. To proceed type (echo \"I am number <digit>\") in the terminal",
        "flag" : "I am number 4", 
        "hint" : "tool | wc -l or AWK, for flag.. echo \"city\" | rev"
    },
    {
        "question": "What city has the most inhabitants? md5sum the word of the city as stated in the file",
        "flag" : "1c0dd63497fdcf1b2843f3ecf646c37c", 
        "hint" : "tool | wc -l or AWK"
    },
    {
        "question": "What is the most common name in the dataset?, print it backwards on the terminal",
        "flag" : "leahciM", 
        "hint" : "tool | sort or AWK"
    },
    {
        "question": "What town has only one inhabitant.. base64 his name",
        "flag" : "SGVucmljCg==", 
        "hint" : "echo \"name\" | base64.."
    },

]

#with open("challenge.json","w") as f:
#    json.dump(challenges,f)
challenges_str = json.dumps(challenges)

# Encode the string to bytes
challenges_bytes = challenges_str.encode('utf-8')

# Base64 encode the bytes
encoded_data = base64.b64encode(challenges_bytes)

with open("challenge.json", "wb") as f:  # Note the 'wb' for write bytes
    f.write(encoded_data)
