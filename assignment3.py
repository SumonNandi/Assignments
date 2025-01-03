'''Conditional Statements
Please write Python Programs for all the problems .
1.	 Take a variable ‘age’ which is of positive value and check the following:
a.	If age is less than 10, print “Children”.
b.	If age is more than 60 , print ‘senior citizens’
c.	 If it is in between 10 and 60, print ‘normal citizen’ '''

#ANS:-
Age = 28
if Age <10:
    print("Children")
elif Age > 60:
    print("senion citizens")
elif Age >=10 and Age <60:
    print("normal citizens")

'''2.	Find  the final train ticket price with the following conditions. 
a.	If male and sr.citizen, 70% of fare is applicable
b.	If female and sr.citizen, 50% of fare is applicable.
c.	If female and normal citizen, 70% of fare is applicable
d.	If male and normal citizen, 100% of fare is applicable'''

#ANS:-
def final_ticket_price(gender,age, citizen, fare):
    if age >=60:
        print("sr.citizen: ")
    elif age <60:
        print("normal citizen: ")
    if gender == 'male' and age >= 60 and citizen == 'sr.citizen':
        print(f"fare of the train is: {fare * 0.7}")
    elif gender == 'female' and age >=60 and citizen == 'sr.citizen':
        print(f"fare of the train is: {fare * 0.5} ")
    elif gender == 'female' and age <60 and citizen == 'normal citizen':
        print(f"fare of the train is: {fare * 0.7}")
    elif gender == 'male' and age <60 and citizen == 'normal citizen':
        print(f"fare aplicable: {fare}")
    else:
        ("input valid details please ")

age= int(input("Enter your age: "))
gender = input("Enter your gender (male/female): ").lower()
citizen = input("Enter your citizenship status (sr.citizen/normal citizen): ").lower()
fare= 5000
final_ticket_price(gender, age, citizen, fare)

#3.	Check whether the given number is positive and divisible by 5 or not.  
number = int(input("Enter the number: "))
number = 0
if number <=0 and number % 5 == 0:
    print("True")

#Please implement Python coding for all the problems.

#1.	A) list1=[1,5.5,(10+20j),’data science’].. Print default functions and parameters exist in list1.

list1=[1,5.5,(10+20j),'data science']

print(dir(list1))

#) How do we create a sequence of numbers in Python?

#ANS:- we can create a sequence of numbers in python using- list,tuple,range and loops.

#)  Read the input from keyboard and print a sequence of numbers up to that number

num = 9
for num in range(0,9):
    num += 1
    print(num)

'''2.	Create 2 lists.. one list contains 10 numbers (list1=[0,1,2,3....9]) and other 
list contains words of those 10 numbers (list2=['zero','one','two',.... ,'nine']).
 Create a dictionary such that list2 are keys and list 1 are values..'''

#Ans:- 
list1 = [1,2,3,4,5,6,7,8,9]
list2 = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Seven", "Eight", "Nine"]

list3 = dict(zip(list2, list1))
print(list3)

'''Consider a list1 [3,4,5,6,7,8]. Create a new list2 such that Add 10 to the even number and
 multiply with 5 if it is an odd number in the list1..'''

list1 = [3,4,5,6,7,8]

for i in (list1):
    if i % 2 == 0:
        print(f" added even numbers are: {i + 10}")
       
for i in (list1):       
     if i % 2 != 0:
        print(f"Multiply numbers are: {i * 5}")

''' 4.Write a simple user defined function that greets a person in such a way that :
i) It should accept both the name of the person and message you want to deliver.
ii) If no message is provided, it should greet a default message ‘How are you’
Ex: Hello ---xxxx---, How are you  -🡪 default message.
Ex: Hello ---xxxx---, --xx your message xx---'''

#ANS:-
def Greeting_person(Name, Massage= "Thank You For Visiting"):

    print(f"your name is {Name} and your massage is {Massage}")

Name = input ("Enter Your name here: ")
Massage = input("Enter Your massage here: ")

Greeting_person(Name, Massage ="Thank You For Visiting")
