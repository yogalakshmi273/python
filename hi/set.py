#syntax
myset = {"apple", "banana", "cherry"}

thisset = {"apple", "banana", "cherry"}#the items will appear in a random order.
print(thisset)#output:{'banana', 'cherry', 'apple'}

#duplicates not allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)#output:{'banana', 'cherry', 'apple'}

#True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)#output:{True, 2, 'banana', 'cherry', 'apple'}

#False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)#output:{False, True, 'cherry', 'apple', 'banana'}

#get the length of sets
thisset = {"apple", "banana", "cherry"}
print(len(thisset))#output:3

#set item
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)#output:{'cherry', 'apple', 'banana'}
print(set2)#{1, 3, 5, 7, 9}
print(set3)#{False, True}

#type
myset = {"apple", "banana", "cherry"}
print(type(myset))#output:<class 'set'>

#access set item
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)#output:apple
#banana
#cherry

#Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)#true

#Check if "banana" is NOT present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)#output:false

#add set items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)#output:{'orange', 'banana', 'apple', 'cherry'}

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)#output:{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

#remove item
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)#output:{'cherry', 'apple'}

#discard method
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)#output:{'cherry', 'apple'}

#pop method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal
#output:banana
#{'apple', 'cherry'}

#clear method:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)#output:set()

#loop items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)#output:apple
#cherry
#banana

#join sets
#union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)#output:{'c', 'a', 2, 3, 'b', 1}

#use to | join two sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)#output:{'a', 3, 1, 'c', 2, 'b'}


x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)#output:{2, 3, 1, 'c', 'b', 'a'}

#update
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)#output:{1, 'a', 3, 2, 'c', 'b'}

#intersection
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)#output:{'apple'}

#Use & to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)#output:{'apple'}

#Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)#output:{False, True, 'apple'}

#difference
#Keep all items from set1 that are not in set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)#output:{'banana', 'cherry'}

#Use - to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)#output:{'banana', 'cherry'}

#symmetric_difference
#Keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)#output:{'google', 'banana', 'microsoft', 'cherry'}

#Use ^ to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)#output:{'google', 'banana', 'microsoft', 'cherry'}

#creat a frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))#output:frozenset({'banana', 'cherry', 'apple'})
#<class 'frozenset'>


