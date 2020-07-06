##Dictionary
# name counter - histogram
namecounter=dict()
# name=input("enter a name: ")
names=['lili','oali','yui','hasami','yui','lili']
for name in names:
    if name not in namecounter:
        namecounter[name] = 1
    else:
        namecounter[name] += 1

print(namecounter)
# get method
# default value if key does not exist
# namecounter.get(name,0)
for name in names:
    namecounter[name]=namecounter.get(name,0)+1
print(namecounter)

# loop through a dictionary
# two iteration variables
name = input("Enter file:")
handle=open(name)
counts= dict()
for line in handle:
    words= line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1
bigcount= None
bigword= None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print(bigword,bigcount)
