import subprocess
import json
from alive_progress import alive_bar 
import os

def main():

    with open("/home/ctf/challenge.json") as db:
        challenges = json.load(db)

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
