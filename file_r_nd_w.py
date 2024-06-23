fhand = open('water.txt')
c = 0
for l in fhand:
    c = c + 1
print("count =", c)

fleg = open('water.txt')
for a in fleg:
    print("chicken")
#quit()
print("ball")

ftake = open('email.txt')
for i in ftake:
    i = i.rstrip()
    if not i.startswith('From ') : continue
    word = i.split()
    print(word[2])
    print(word)