grades = {
    'Alice': 95,
    'Bob': 85,
    'Charlie': 92
}

print(grades['Alice'])  # Output: 95

# Adding a new key-value pair
grades['David'] = 88
grades['Bob'] = 11
print(grades)

#Counting in dictionary

count = dict()
gradesss = ['Alice','Bob','Charlie','Alice','Bob']
for i in gradesss:
    count[i] = count.get(i, 0) + 1
print(count)
#else:
  #  x = 0
#x = grades.get(name, 0)

#looping in dictionary
for j in count:
    print(j, count[j])

print(count.values())
print(count.keys())

#using items will give both key nd value access together
for l,m in count.items():
    print(l,"and", m)


fname = input("enter file name:")
if len(fname) < 1 : fname = 'clown.txt'
ball = open(fname)

di = dict()
for line in ball:
    line = line.rstrip()
    #print(line)
    words = line.split()
    #print(words)
    for w in words:
        if w in di :
            di[w] = di[w] + 1
            print("existing")
        else:
            di[w] = 1
            print("new!!!!")
        print(w, di[w])

print(di[w])

 