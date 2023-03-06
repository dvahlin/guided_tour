#!/bin/bash
while true; do
    read -s -p "Ready? if so just type yes: "
    echo -e "\n"
    if [[ $REPLY == yes ]]; then
        exit
    else
	echo -e "No rush"
        continue   
    fi
done
