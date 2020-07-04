"""
Lists
    - mutable = changeable
    - elements of a list can be of multiple types

"""
# Concatenating lists using  '+'
li1=[1,2,3]
li2=[4,5,6]
li_sum=li1+li2
print(li_sum)

# slicing a list
# li[start:end] - up to but not including 'end'
sl_full=li_sum[:]
sl_01=sl_full[:4]
sl_02=sl_full[4:7]
# list Methods
# append
li1.append('added')
print(li1)
# Is Something in a list?
print(1 in li1)
print(0 not in li1)
# sort the list
li_alpha= ['o','l','i','v']
li_alpha.sort()
print(li_alpha)
# use data structure to count and calculate mean
numlist=[]
while True:
    num= input("Please enter a number (enter 'done'to quit): ")
    if num == 'done' : break
    numlist.append(float(num))
average = sum(numlist)/len(numlist)
print('Average:',average)

