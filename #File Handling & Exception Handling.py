#File Handling & Exception Handling

#1)Write the code in python to open a file named “try.txt”

f = open("try.txt", "r")
data = f.read()
f.close()
print(data)

#2)What is the purpose of ‘r’ as a prefix in the given statement? 
# f = open(r, “d:\color\flower.txt”)

#ANS:- Here 'r' is to read the file only

#3)Write a note on the following
'''A.	Purpose of Exception Handling
B.	Try block
C.	Except block
D.	Else block
E.	Finally block
F.	Built-in exceptions'''

#A.-ANS:- Exception Handeling is the way to avoid errors during the execution of the program.
#purpase:- a- Handel unpredictable problems, b- Handel program crases, c- To make sure to data loss

#B:- Try block is a part of code that handel the errors that could be created during the code execution.
#purpase:- a- Identify errors, b- Ensure errors could handel.

#C:-  Here Except block is a part of code to avoid the beforehand errors using some keywords
# purpase:- a- To get a  errorless answer, b- To handel reduce the risk of errors

#D:- Here Else block works if no exception occurs

#E:- Finally block used to cleanup the code that executed . Finally block don't look back to the exceptions.

#F:- Buil-in exceptions are predifined errors that can occurs in execution of the program.

#4) Write 2 Custom exceptions

#ANS:- Two custom exceptions are:-
#1- ZeroDvisionError,2- TypeError, 3- NameError

