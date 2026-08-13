name = "Yhomi"
age = 30

if age >= 18:
    print("You are an adult")

country = "Nigeria"
print(country)
print(age)
print(name)
print(type(name))
print(type(age))
print(type(age))
balance = 1500000
print(type(balance))
height = 1.75
print(type(height))
is_learning = True
print(type(is_learning))
if is_learning:
    print("I am learning Python")
else:
    print("I am not learning Python")

score = 40

if score >= 80:
    print("Excellent")
elif score >= 50:
    print("You passed")
else:
    print("You failed")

    age = 30
has_id = True

if age >= 18 and has_id:
    print("You can enter")
else:
    print("You cannot enter")

has_ticket = False
is_guest = True

if has_ticket or is_guest:
    print("You can enter the event")
else:
    print("You cannot enter the event")

is_busy = False

if not is_busy:
    print("I am available")

country = "Nigeria"

if country == "Nigeria":
    print("Country matches")

if country != "Ghana":
    print("Country is not Ghana")

if age > 18:
    print("Age is greater than 18")

if age < 40:
    print("Age is less than 40")

if age >= 18:
    print("Age is 18 or older")

if age <= 40:
    print("Age is 40 or younger")

skills = ["Python", "AI", "SQL"]
print(skills)

print(skills[0])

print(skills[1])
print(skills[2])

skills.append("JavaScript")
print(skills)

skills.remove("SQL")
print(skills)

print(len(skills))

skills[0] = "Python Programming"
print(skills)

for skill in skills:
    print(skill)

for skill in skills:
    if skill == "AI":
        print("Found AI!")

for number in range(5):
    print(number)

for number in range(1, 6):
    print(number)

person = {
    "name": "Yhomi",
    "age": 30,
    "country": "Nigeria"
}

print(person)

print(person["name"])
print(person["age"])
person["age"] = 31
print(person["age"])
person["skill"] = "Python"
print(person)

person.pop("skill")
print(person)

def greet():
    print("Hello from RobotChat!")

greet()

def greet(name):
    print(f"Hello, {name}!")

greet("Yhomi")

def introduce(name, country):
    print(f"My name is {name} and I am from {country}.")

introduce("Yhomi", "Nigeria")

def add_numbers(a, b):
    return a + b

result = add_numbers(10, 5)
print(result)

def multiply(a, b):
    return a * b

answer = multiply(6, 4)
print(answer)

def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

result = check_age(30)
print(result)

def show_skills(skills):
    for skill in skills:
        print(skill)

show_skills(["Python", "AI", "SQL"])

def get_skills():
    return ["Python", "AI", "SQL"]

my_skills = get_skills()
print(my_skills)

user_name = input("What is your name? ")
print(f"Hello, {user_name}!")

age = int(input("How old are you? "))
print(type(age))

age = int(input("How old are you? "))
print(type(age))

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

if age >= 30:
    print("You are 30 or older")
else:
    print("You are under 30")

if age >= 60:
    print("You are a senior")
elif age >= 30:
    print("You are an adult")
else:
    print("You are young")

if age >= 60:
    print("You are a senior")
elif age >= 30:
    print("You are an adult")
else:
    print("You are young")

if age >= 60:
    print("Senior")
elif age >= 30:
    print("Adult")
elif age >= 18:
    print("Young adult")
else:
    print("Minor")

has_id = False

if age >= 18 and has_id:
    print("You can enter")
else:
    print("You cannot enter")
    print(has_id)
has_ticket = False
is_guest = False

if has_ticket or is_guest:
    print("You can enter the event")
else:
    print("You cannot enter the event")

    is_busy = False

if not is_busy:
    print("I am available")
else:
    print("I am busy")