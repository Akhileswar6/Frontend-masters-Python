#list
names=["akhil","repos","nina"]
print(len(names))

#indexing
print(names[1])
print(names[2])

#updating an item in list
names=["Nina", "Max", "Jane"]
names[2]="akhil"
print(names)

#formatting
names=[
    "nina",
    "Akhil",
    "jane"
    ]

#sorting
lottery_numbers=[1,3,4,65,87,23,2,3426,876,84]
print(sorted(lottery_numbers))

#reverse
print(sorted(lottery_numbers, reverse=True))
lottery_numbers.reverse()

lottery_numbers=[1,2,3,56,78,98,23,109,34,11]
lottery_numbers.sort()
print(lottery_numbers)

words=["umbrella", "fox", "apple"]
words.sort()
print(words)

print(dir(list))
print(help(list.append))

names = ["Nina", "Max"]
names.append("John")
names.insert(0,"akhil")
print(names)

#extend
names1=["akhil","Nina","john","shiva"]
colours=["Red","yellow","white","pink"]
names1.extend(colours)
print(names1)

#looking for items
names2=["akhil","Nina","john","shiva"]
a="Nina" in names2
print(a)

ab=names.index("Nina")
print(ab)

a1=names.remove("Nina")
print(a1)

names.pop()
print(names)


#tuples
a=()
print(type(a))

b=(1)
print(type(b))

c=(9,)
print(type(c))

student=("Marcy",76,"akhil",32,87.6)
print(student[1])

student1=["Marcy",34,"History",9.8]
name,age,subject,grade=student1
print(name)
print(age)
print(subject)
print(grade)

def http_status_code():
    return 200,"OK"
code,value=http_status_code()
print(code)
print(value)


#sets
my_set={}
print(type(my_set))

my_set1=set()
print(type(my_set1))

names3={"Nina","akhil","Nina"}
print(names3)
print(len(names3))

i=hash("Nina")
print(i)

colours=["red","yellow","red","green","blue","green","green"]
print(set(colours))

my_sets={1,"a",2,"b",3,"c"}
print(my_sets)

my_set = {"a", "b", "cat", "dog", "red"}
print(sorted(my_set))

colors = {"Red", "Green", "Blue"}
colors.add("Orange")
print(colors)

colors = {"Red", "Green", "Blue"}
colors.discard("Green")
print(colors)

colors = {"Red", "Green"}
numbers = {1, 3, 5}
colors.update(numbers)
print(colors)

numbers = {1, 3, 5}
numbers.update("hello")
print(numbers)

rainbow_colors = {"Red", "Orange", "Yellow", "Green", "Blue", "Violet"}
favorite_colors = {"Blue", "Pink", "Black"}

print(rainbow_colors | favorite_colors)

print(rainbow_colors & favorite_colors)

print(rainbow_colors ^ favorite_colors)


#Dictionaries
my_dict={}
print(type(my_dict))

nums = {1: "one", 2: "two", 3: "three"}
print(len(nums))
print(nums[1])
print(nums[2])

nums = {1: "one", 2: "two", 3: "three"}
print(nums.get(4, "default"))

colors = {"r": "Red", "g": "Green"}
numbers = {1: "one", 2: "two"}
colors.update(numbers)
print(colors)

colors={"Green":["Spinach"]}
print(colors)
colors["Green"].append("Apples")
print(colors)

#getting all keys in a dictionary
nums={1:"one",2:"two",3:"three",8:"eight"}
print(nums.keys())

#getting all the values in a dictionary
nums={1:"one",2:"two",3:"three",8:"eight"}
print(nums.values())

#getting all the items (key,value pair)
nums={1:"one",2:"two",3:"three",8:"eight"}
print(nums.items())





a=6
b="akhil"
print(str(a)+b)



