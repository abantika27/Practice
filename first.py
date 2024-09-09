# print("Hello, World!")
# i am learning python

#comparison operators
d = 5==5
print(d)

#logical operators
print("True or False is ", True or False)
print("True or True is ", True or True)
print("False or True is ", False or True)
print("False or False is ", False or False)
print("False or False is ", False or False)
print("False or False is ", False or False)

a = "31.2"
b = float(a) 
t = type(b) # type of b

#by default input is string
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
print("The square of the number is", a**2) #a^2 would be incorrect
print("Number a is: ", a)
print("Number b is: ", b) 
print("Sum is ", a + b)

name = "Harry"
# name[1]= "a" #this will give an error as strings are immutable
print(name[0:3])

#same
print(name[-4: -1])
print(name[1:4])

name = input("Enter your name: ")
#fstring to use instead of print("Good morning, ", name)
print(f"Good morning, {name} ") 


#list are mutable
friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends[0:4])

#tuple are immutable
tp = (1, 2, 3, 4)
print(tp)

d = {} # Empty dictionary
marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23
}
print(marks["Harry"])

e = set() # Dont use s = {} as it will create an empty dictionary
s1 = {1, 5, 32, 54,5, 5, 5} 

s2 = {7, 8, 1, 78}

print(s1.union(s2))
print(s1.intersection(s2))

#if else
p1 = "click here"
p2 = "buy now"  

message = input("Enter your comment: ")

if((p1 in message) or (p2 in message )):
    print("This comment is a spam")

else:
    print("This comment is not a spam")

n = int(input("Enter a number: "))

for i in range(100):
    if(i == 34):
        break # Exit the loop right now
    print(i)

for i in range(100):
    if(i == 34):
        continue # Skip this iteration
    print(i)    

for i in range(2, n):
    if(n%i) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")




