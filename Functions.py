def hello_world():
    print("Hello,world")
hello_world()

def add_nums(x,y):
    return x+y
x=98
y=4
sums=add_nums(x,y)
print(sums)

def foo():
    x=9
    return 
val=foo()
print(type(val))
print(val)

def add_numbers(x, y):
    return x + y
new_num=add_numbers(3, 5)
print(new_num)

#functional arguments
def say_greeting(name, greeting):
    print(f"{greeting}, {name}.")
say_greeting("Hello", "Nina")

#keyword with default values
def say_greeting(name="akhil", greeting="Hello", punctuation="!"):
    print(f"{greeting}, {name}{punctuation}")
say_greeting()

def create_query(language="Javascript", stars=5, sort="desc"):
    return f"Language:{language}, Stars:{stars}, Sort:{sort}"
print(create_query())
print(create_query(language="Ruby"))
print(create_query("python"))

def add_five_to_list(my_list=[]):
    my_list.append(23)
    return my_list
print(add_five_to_list())
print(add_five_to_list())


#scope inside a function
def twitter_info():
    twitter_account="coders"
    return f"Account inside function: {twitter_account}"
print(twitter_info())
"""print(f"Account outside of function: {twitter_account}")"""

#using variables defined outside of the function
name="nina"
print(f"name outside of function: {name}")

def try_change_name():
    name="akhil"
    print(f"name inside of function: {name}")
print(try_change_name())

print(f"name outside of function: {name}")


ROOT_API_URL= "https://api.github.com"
def api_search_repos_url():
    return f"{ROOT_API_URL}/search/repositories"
print(api_search_repos_url())

#Positional arguments vs Keyword arguments
def calculate_numbers(x, y, operation="add"):
    if operation=="add":
        return x + y
    elif operation=="subtract":
        return x - y
print(calculate_numbers(3,70))
print(abs(calculate_numbers(2,67,"subtract")))










