import subprocess
import json
import os
import re
import select
import base64
from alive_progress import alive_bar, config_handler
from re import search
import pyfiglet

def main():
    with open("/home/ctf/challenge.json", "r") as f:
        encoded_data = f.read()
    
    decoded_data = base64.b64decode(encoded_data)
    challenges = json.loads(decoded_data)
    
    f = subprocess.Popen(["tail", "-F", "/var/tmp/ctf.log"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    with alive_bar(
        len(challenges),
        title="Progress",
        bar="classic",
        stats=False,
        elapsed=False,
    ) as bar:
        while True:
            try:
                current = challenges[0]
                if "display_question" not in current.keys():
                    os.system('cls||clear')
                    header = pyfiglet.figlet_format("CTF Challenge", font="slant")
                    print("\033[1;34m" + header + "\033[0m")  # Blue color
                    print("\033[1;36m" + current["question"] + "\033[0m")  # Cyan color
                    current["display_question"] = True

                if select.select([f.stdout], [], [], 0.5)[0]:
                    try:
                        line = f.stdout.readline().decode("utf-8").strip()
                    except UnicodeDecodeError:
                        continue

                    if search("hint", line):
                        print("\033[1;33m" + current["hint"] + "\033[0m")  # Yellow color

                    flag_pattern = re.compile(''.join(current["flag"]))
                    if flag_pattern.search(line):
                        challenges.pop(0)
                        bar()
                        open("/home/ctf/.bash_history", "w").close()
            except IndexError:
                footer = pyfiglet.figlet_format("Victory!", font="univers")
                print("\033[1;31m" + footer + "\033[0m")  # Red color
                os.system("sleep 5 && killall -u ctf")
                break

if __name__ == '__main__':
    main()
