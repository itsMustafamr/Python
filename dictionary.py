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


    #best way just use di[w] = dii.get(w, 0) + 1 (all in 1)

print(di[w])

#now to find the most common word
largest = -1
for k,v in di.items():
    print(k, v)
    if v > largest:
        largest = v
        the_largest_word = k
    else:
        break

print('Done', the_largest_word, largest)

x = sorted(di.items())
print(x)

temp = list()
for k,v in di.items():
    newt = (v,k)
    temp.append(newt)

print('flipped',temp)

temp = sorted(temp)
print("sorted", temp)

temp = sorted(temp, reverse=True)
print("Sorted in reverse", temp[:5], "this gives the top 5(upto but not 5)")
print(" ") 
for v,k in temp[:3]:
    print(k,v)

