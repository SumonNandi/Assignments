#Regular Expression
#1)Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)	

import re

pan = "BJLPN9335A"

pattern = (r'^[A-Z][a-z][0-9]')

if re.match(pattern, pan):
    print("This is a pan card")
else:
    print("Please input a valis pan number")

#2) Write a Python program to replace all occurrences of space, comma, or dot with a colon

string = "Hi, Sangita how are you."

str = re.sub(r"[ , .]", ":", string)
print(str)
  