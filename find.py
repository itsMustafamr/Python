hand = open("email.txt")
for line in hand:
    line = line.rstrip()
    if line.find("From") >= 0:
        print(line)
    else:
        break

import re
hand = open("email.txt")
for line in hand:
    line = line.rstrip()
    if re.search("From", line) :
        print(line)

