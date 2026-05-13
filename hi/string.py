a = "Hello, World!"#it take the array index based in output.
print(a[1])

a = "Hello, World!"#length of a value
print(len(a))#output:13

txt = "The best things in life are free!"
print("free" in txt)#it check the word is there are not in the txt value
#output:true

txt = "The best things in life are free!"
print("expensive" not in txt)#output:true

#slicing string
b = "Hello, World!"#positive index read in left to right start (0)
print(b[2:5])#output:llo 

b = "Hello, World!"
print(b[:5])#output:Hello

b = "Hello, World!"
print(b[2:])#output:llo, World!

#negative index
b = "Hello, World!"#negative index read in right to left start (-1)
print(b[-5:-2])#output:orl

#modify string
#upper case
a = "Hello, World!"
print(a.upper())#output:HELLO, WORLD!

#lower case
a = "Hello, World!"
print(a.lower())#output:hello, world!

#remove whitespaces
a = " Hello, World! "
print(a.strip()) #output:Hello, World!

#replace
a = "Hello, World!"
print(a.replace("H", "J"))#output:Jello, World!

#split string
a = "Hello, World!"
b = a.split(",")
print(b)#output:['Hello', ' World!']

#cancatenate of string
a = "Hello"
b = "World"
c = a + b
print(c)#output:HelloWorld

#string between space
a = "Hello"
b = "World"
c = a + " " + b
print(c)#output:Hello World

#format string
age = 36
txt = f"My name is John, I am {age}"# use number in sting must uesd in curly bases{}.
print(txt)#output:My name is John, I am 36

price = 59
txt = f"The price is {price:.2f} dollars"# .2f used in add .00
print(txt)#output:The price is 59.00 dollars

#escape character
txt = "We are the so-called \"Vikings\" from the north."
print(txt) #must ues in \ otherwise the output not show in inside double quotes word.
#output:We are the so-called "Vikings" from the north.

#boolean
print(10 > 9)
print(10 == 9)
print(10 < 9)#output:True,False,False

print(bool("Hello"))#output:true. because the value is not exit
print(bool(15))#true. there is no empty and zero

#isinstance
x = 200 #check the object is integer or not
print(isinstance(x, int))#output:true

def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")#output:true