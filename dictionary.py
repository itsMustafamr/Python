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

 