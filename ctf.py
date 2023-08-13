import subprocess
import json
import os
import re
import select
import base64
from alive_progress import alive_bar
from re import search

def main():
    with open("/home/ctf/challenge.json", "r") as f:
        encoded_data = f.read()
    
    decoded_data = base64.b64decode(encoded_data)
    challenges = json.loads(decoded_data)
    
    f = subprocess.Popen(["tail", "-F", "/var/tmp/ctf.log"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    with alive_bar(
        len(challenges),
        title="Progress",
        bar="checks",
        stats=False,
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
                # Check if there's new data available to read
                #   print("Waiting for new data...")
                if select.select([f.stdout], [], [], 1.0)[0]:
                    try:
                        line = f.stdout.readline().decode("utf-8").strip()
                    except UnicodeDecodeError:
                        # Handle the error for reading binary
                        continue

                    #print("Received data: ", line) 
                    if search("hint", line):
                        color = "\033[1;33m \n"
                        print(current["hint"] + color)

                    flag_pattern = re.compile(''.join(current["flag"]))
                    if flag_pattern.search(line):
                    #if search(''.join(current["flag"]), line):
                        challenges.pop(0)
                        bar()
                        open("/home/ctf/.bash_history", "w").close()
            except IndexError:
                print(r""" 
                             _|      _|  _|              _|                                    
                             _|      _|        _|_|_|  _|_|_|_|    _|_|    _|  _|_|  _|    _|  
                             _|      _|  _|  _|          _|      _|    _|  _|_|      _|    _|  
                               _|  _|    _|  _|          _|      _|    _|  _|        _|    _|  
                                 _|      _|    _|_|_|      _|_|    _|_|    _|          _|_|_|  
                                                                                           _|  
                                                                                       _|_|    
                            
                            """)                       
                os.system("sleep 5 && killall -u ctf")
                break

if __name__ == '__main__':
    main()
