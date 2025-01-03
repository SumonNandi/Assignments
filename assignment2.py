#Data Types
#Please implement it by using Python.
#1.	Construct 2 lists containing all the available data types  (integer, float, string, complex and Boolean) and do the following..



list1 = [143, 195.5, "Sangita", 3+6j, True]
list2 = [143, 143.3, "Dilip", 5+10j, False]


#a.	Create another list by concatenating above 2 lists

new_list = list1 + list2
print(new_list)

#b.	Find the frequency of each element in the concatenated list.

frequency = {}
for i in new_list:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print("Frequency of each element:", frequency)

#c.	Print the list in reverse order.
new_list.reverse()
print(new_list)


#2.	Create 2 Sets containing integers (numbers from 1 to 10 in one set and 5 to 15 in other set)

#a.	Find the common elements in above 2 Sets.

set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {5,6,7,8,9,10,11,12,13,14,15}

com_el = set1.intersection(set2)
print(com_el)

#b.	Find the elements that are not common.

Not_cm = set1 ^ set2
print(Not_cm)

#c.	Remove element 7 from both the Sets.

set1.discard(7)
set2.discard(7)

#3.	Create a data dictionary of 5 states having state name as key and number of covid-19 cases as values.
#a.	Print only state names from the dictionary.

Dict1 ={'Mumbai': 45890, 'West Bengal': 58094, 'Delhi': 78874, 'chennai':123980, 'Bangalore': 982340}

print(Dict1.keys())

#b.	Update another country and its covid-19 cases in the dictionary.

Dict1['Utter Pradesh'] = 298746
print(Dict1)

#Please implement by using Python
#1.	A. Write an equation which relates   399, 543 and 12345 

a = 399
b = 543
c = 12345

eqn = (a*b+c)
print(eqn)

#B. “When I divide 5 with 3, I get 1. But when I divide -5 with 3, I get -2”—How would you justify it?

'''ANS:- When I divide 3, I get 1 because here "1" is floor division(//) but here "2" is 
remainder(%)'''

#Exmp:-
a = 5
b = 3
print(a%b)
print(a//b)


#2. a=5,b=3,c=10.. What will be the output of the following:
# A. a/=b ,  B. c*=5  
      
a = 5
b = 3
c= 10
a = a/b
print(a)

c = c*5
print(c)


#3. A. How to check the presence of an alphabet ‘S’ in the word “Data Science” .

alph = "data Science"

alph2 = "S"

count = alph.count(alph2)
print(count)

#B. How can you obtain 64 by using numbers 4 and 3 .

#Ans:-
a = 4
b = 3
c= 4**3
print(c)

#Please implement by using Python
#1.	What will be the output of the following (can/cannot):
#a.	Age1=5
#b.	5age=55

#ANS:- 
Age1 = 5
print(Age1)#---(can)
#In python, variable should start with a letter and using underscore only so Age1 =5 can print.

#5age = 55 ---(cannot)
 # Here 5age variable can not give any output here because of syntaxerron.

#2.	What will be the output of following (can/cannot):
#a.	Age_1=100
#b.	age@1=100

#ANS:- 

Age_1 = 100 #---(can)
print(Age_1) #In python Age_1 can print without syntaxerror because it's statring with a letter and also has an uderscore.

#age@1=100 --- (cannot)
#print(age@1) - In python we can use only underscore in variable,no other spacial character can use.

#3.	How can you delete variables in Python ?

#ANS:- We can delete variables in python using (del- keyword)
#EXMP:-
variable = "Sumon"
print(variable)
del variable



             


