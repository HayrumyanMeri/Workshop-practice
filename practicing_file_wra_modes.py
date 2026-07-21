import sys

f = open("mytext.txt", "a+")
f.write("line 4")
my_data = f.read()
print(my_data)
f.close()