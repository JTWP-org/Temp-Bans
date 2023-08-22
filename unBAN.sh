#this uses bash to just set a cmd to run on a set day to unban the user  it just removes it from the blackklist.txt not a rcon ... because i was lazy

#!/bin/bash

echo "sed -i "/$2/d" /home/steam/cfg/blacklist.txt" | at today +${1} days
