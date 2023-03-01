import subprocess
from alive_progress import alive_bar 
import os

def main():
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

    f = subprocess.Popen(["tail", "-F", "/home/ctf/.bash_history"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    with alive_bar(
            len(challenges),
            title="Progress",
            bar="checks",
            stats=False,
            #monitor=False,
            elapsed=False,
            ) as bar:
        
        while True:
            try:
                current = challenges[0]
                if "display_question" not in current.keys():
                    os.system('cls||clear')
                    color = "\033[1;36m \n"
                    print(current["question"] + color)
                    current["display_question"] = True

                line = f.stdout.readline().decode("utf-8").strip()

                if line == "hint":
                    color = "\033[1;33m \n"
                    print(current["hint"] +color)

                if line in current["command"]:
                    challenges.pop(0)
                    bar()
                    open("/home/ctf/.bash_history", "w").close()

            except IndexError:
                print("VICTORY!")
                break

if __name__ == '__main__':
    main()
