#data_types


# integers
2,5,6376,7,9,6537,90,50,5,8,4,7

#float
0.5,65.0,4.8,5.0

#strings
"leon"
"father"
"apple"
"fruits"
"eily"
"orange"

#boolean
True
False


#VARIABLES

score=30
name = "Dean"
school="E Blue"
age =34
location="budiriro"
height=5.8
city="harare"
x=7
y=True



print(name )
print(score)
print(school)
print(age)
print(location)
print(city)
print(height)
print(x)
print(y)



print(type(x))
print(type(y))
print(type(name))
print(type(location))
print(type(height))
print(type(school))
print(type(score))
print(type(city))
print(type(age))

n=6
z=4
print(f"addition {n+z}")
print(f"subtraction {n-z}")
print(f"multiply {n*z}")
print(f"division {n/z}")
print(f"modulus {n%z}")
print(f"expo {n**z}")

#operators


#lists
groceries= ["cereals","cooking oil","snacks"]
print(groceries)



#index
print(groceries[0])


#slicing list

groceries.append("fruits")
print(groceries)


groceries.remove("cooking oil")
print(groceries)



groceries.insert(1,"juice")
print(groceries)


books=["chemistry","biology","music"]
print(books)

books.reverse()
print(books)


books.clear()
print(books)




#sets

juices={"revive","cascade","coke"}
print(juices)
print(len(juices))
print("funfresh" in juices)
print("coke" in juices)



juices.add("funfresh")
print(juices)


juices.remove("coke")
print(juices)

even_num={"2","4","6"}
print(even_num)


even_num.add("8")
even_num.remove("4")

print(even_num)



#tuples

shoes=("nike","jordan","addidas","nike")
print(shoes)

print(shoes.index("jordan"))
print(shoes.count("nike"))



#dictionaries

designer={
    "name":"Mejury",
    "age":34,
    "location":"Zvishavane",
}

print(designer)
print(designer["location"])

school_uniforms={
    "errymaple":"blue",
    "marian":"red",
}
print(school_uniforms)

school_uniforms.pop("marian")
print(school_uniforms)

school_uniforms.clear()
print()


#if statements
register= "present"
name ="Leon"

if register == "present":
    print(f'{name} is {register}')


x=5
x>10
if x>10:
    print(True)
else:
    print(f"{x} is than 10")



password  =4536

if password==4536:
    print("welcome")
else:
    print("invalid password")    
  
#while loops 

num =int(input("Enter a number between 1-10:"))
while num <1 or num > 10:
     print (f"(num) is not valid")

     num =int(input("Enter a number between 1-10:"))
     print(f"Your num is{num}")


num = 100
while num >= 1:
    print(num)
    num-=1

num =1
while num <=100:
    print(num)
    num+=1     



     #for loops
for n in range(5):
         print(n)
fruits=["banana" ,"apple" ,"cherry"]
for fruit in fruits:
      print(fruit)


      
fruits =["a","b","c"]
for fruit in fruits:
    print(fruit)

text =["Code"]
for char in text:
    print(char) 

for x in range (1-11):
    print (x) 




#functions
def happy_birthday(name,age):
    print(f"happy birthday to {name}")
    print(f"you are{age} years old")
    print("happy birthday to you") 



happy_birthday("Vyie",18)  





def greet():
    print("Hello, welcome to Python!")

greet() 


def greet(name):
    print(f"hello,{name}!")

greet("Mejury")
greet("Elsie")    


def add(a,b):
    return a + b
result = add(4,3)
print(result)


def multiply(a,b):
    return a*b
result = multiply (4,6)
print(result)

      
#nested functions
         
