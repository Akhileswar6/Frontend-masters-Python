#Data types
x="Akhil"
y=98
z=1.98
a=True
b=None

#type()
print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))

#dir()
print(dir(str))
print(dir(int))


#help()
print(help(str.isupper))
print(help(str.title))
print(help(str.endswith))
print(help(str.strip))

#These are all integers
x = 4
y = -193394

#These are all floats
x = 5.0
y = -3983.2

#This is a complex number
z=2+3j
print(type(z))

#int()
aa=int(4)
bb=float(2.45)
l=int('56')
print(type(l))

#Boolean Types
a=True
b=False

#Representing Strings
#Concatenated
Salutation="Hello"
name="Akhil"
print(Salutation + name)

long_greeting = """
                Greetings and salutations, dear Nina.
                I'm superfluous with my words,
                and require more space to say Hello!"
                """

#formatting strings
name="Akhil"
sur_name="Kamale"
print(f"my name is {name} {sur_name}")

my_num=3
print(str(my_num) + " three")

my_str="56"
print(int(my_str) + 3)

rent=480
per_day=rent//30
print(per_day)

name = "Nina"
print("Hello, my name is %s" % name)

name="Akhil"
print(f"hello my name is {name} an i pay ${per_day} in month")





























