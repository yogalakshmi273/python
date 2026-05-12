#syntax
mylist = ["apple", "banana", "cherry"]#list used in square brackets

thislist = ["apple", "banana", "cherry"]
print(thislist)#output:['apple', 'banana', 'cherry']

#allow duplicate
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)#output: ['apple', 'banana', 'cherry', 'apple', 'cherry']

#list length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))#output: 3

#type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))#output:<class 'list'>

#access list item
thislist = ["apple", "banana", "cherry"]
print(thislist[1])#output:banana

#negative index
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])#output:cherry

#range of index
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])#output:['cherry', 'orange', 'kiwi']

#range of negative index
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])#output:['orange', 'kiwi', 'melon']

#check if item is exit
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")#output:Yes, 'apple' is in the fruits list

#change list item
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)#output:['apple', 'blackcurrant', 'cherry']

#change of range list item
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)#output:['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

#insert item  
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")#output:['apple', 'banana', 'watermelon', 'cherry']
print(thislist) 

#add list item
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)#output:['apple', 'banana', 'cherry', 'orange']

#insert item
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)#output:['apple', 'orange', 'banana', 'cherry']

#extend list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)#output:['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

#remove list item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)#output:['apple', 'cherry']

#remove item in pop() used
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)#output:['apple', 'cherry']

#remove item in del used
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)#output:['banana', 'cherry']

#clear
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)#output:[]

#loop list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)#output:apple
#banana
#cherry

#while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#output:apple
#banana
#cherry

#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)#output:['apple', 'banana', 'mango']

#syntax
newlist = [expression for item in iterable if condition == True]

#ex
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)#output:['banana', 'cherry', 'kiwi', 'mango']

newlist = [x for x in range(10) if x < 5]
print(newlist)#output:[0,1,2,3,4]

#upper 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)#output:['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)#output:['hello', 'hello', 'hello', 'hello', 'hello']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)#output:['apple', 'orange', 'cherry', 'kiwi', 'mango']

#sort list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)#output:['banana', 'kiwi', 'mango', 'orange', 'pineapple']

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)#output:[23, 50, 65, 82, 100]

#sort descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)#output:['pineapple', 'orange', 'mango', 'kiwi', 'banana']

#case insensitive sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()#it print first is capital letter words
print(thislist)#output:['Kiwi', 'Orange', 'banana', 'cherry']

#reverse order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) #output:['cherry', 'Kiwi', 'Orange', 'banana']

#copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)#output:['apple', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)#output:['apple', 'banana', 'cherry']

#slice operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)#output:['apple', 'banana', 'cherry']

#join list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)#output:['a', 'b', 'c', 1, 2, 3]

#usinh for loop
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)#output:['a', 'b', 'c', 1, 2, 3]

#using extend
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)#output:['a', 'b', 'c', 1, 2, 3]

#syntax
mylist = ["apple", "banana", "cherry"]#list used in square brackets

thislist = ["apple", "banana", "cherry"]
print(thislist)#output:['apple', 'banana', 'cherry']

#allow duplicate
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)#output: ['apple', 'banana', 'cherry', 'apple', 'cherry']

#list length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))#output: 3

#type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))#output:<class 'list'>

#access list item
thislist = ["apple", "banana", "cherry"]
print(thislist[1])#output:banana

#negative index
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])#output:cherry

#range of index
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])#output:['cherry', 'orange', 'kiwi']

#range of negative index
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])#output:['orange', 'kiwi', 'melon']

#check if item is exit
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")#output:Yes, 'apple' is in the fruits list

#change list item
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)#output:['apple', 'blackcurrant', 'cherry']

#change of range list item
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)#output:['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

#insert item  
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")#output:['apple', 'banana', 'watermelon', 'cherry']
print(thislist) 

#add list item
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)#output:['apple', 'banana', 'cherry', 'orange']

#insert item
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)#output:['apple', 'orange', 'banana', 'cherry']

#extend list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)#output:['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

#remove list item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)#output:['apple', 'cherry']

#remove item in pop() used
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)#output:['apple', 'cherry']

#remove item in del used
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)#output:['banana', 'cherry']

#clear
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)#output:[]

#loop list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)#output:apple
#banana
#cherry

#while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#output:apple
#banana
#cherry

#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)#output:['apple', 'banana', 'mango']

#syntax
newlist = [expression for item in iterable if condition == True]

#ex
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)#output:['banana', 'cherry', 'kiwi', 'mango']

newlist = [x for x in range(10) if x < 5]
print(newlist)#output:[0,1,2,3,4]

#upper 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)#output:['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)#output:['hello', 'hello', 'hello', 'hello', 'hello']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)#output:['apple', 'orange', 'cherry', 'kiwi', 'mango']

#sort list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)#output:['banana', 'kiwi', 'mango', 'orange', 'pineapple']

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)#output:[23, 50, 65, 82, 100]

#sort descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)#output:['pineapple', 'orange', 'mango', 'kiwi', 'banana']

#case insensitive sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()#it print first is capital letter words
print(thislist)#output:['Kiwi', 'Orange', 'banana', 'cherry']

#reverse order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) #output:['cherry', 'Kiwi', 'Orange', 'banana']

#copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)#output:['apple', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)#output:['apple', 'banana', 'cherry']

#slice operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)#output:['apple', 'banana', 'cherry']

#join list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)#output:['a', 'b', 'c', 1, 2, 3]

#usinh for loop
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)#output:['a', 'b', 'c', 1, 2, 3]

#using extend
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)#output:['a', 'b', 'c', 1, 2, 3]

