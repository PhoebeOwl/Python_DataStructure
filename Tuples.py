# # Tuples are immutable
# # When we are making "temporary variables" we prefer tuples over lists
# # Assignment
# (x,y)=(4,'fred')
# print(y)
# # Tuples and Dictionaries
# # The items() method in dictionaries returns a list of
# # (key, value) tuples
# # tuples are comparable
# (0,1,2) < (5,1,2)
# # sort by value instead of key
# # make a temporary list
# c= {'a':10,'b':1,'c':22}
# tmp=list()
# for k,v in c.items():
#     tmp.append((v,k))
# tmp= sorted(tmp,reverse=True)
# print(tmp)
# # The top 10 most common words
# fhand=open("words.txt")
# counts=dict()
# for line in fhand:
#     words=line.split()
#     for word in words:
#         counts[word] = counts.get(word,0) +1
# tmp=[]
# for k,v in counts.items():
#     tmp.append((v,k))
# tmp=sorted(tmp,reverse=True)
# print(tmp[:10])
# # Shorter Version
# # List comprehension creates a dynamic list.
# # In this case, we make a list of reversed tuples and then sort it.
# print(sorted([(v,k) for k,v in c.items()]))


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dis=dict()
for line in handle:
    if line.startswith('From '):
        words=line.split()
        hms= words[5]
        time=hms.split(':')
        hour=time[0]
        dis[hour]=dis.get(hour,0)+1

temp=[]
for k,v in dis.items():
    temp.append((k,v))
temp=sorted(temp)
for ele in temp:
    print(ele[0],' ',ele[1])



