# Write a Python function which generates 26 text files named A.txt, B.txt, and so on up to Z.txt.
import os    # I need this to delete the files after creation if I want to

for i in range(ord('A'), ord('Z') + 1):
    file = open(chr(i)+'.txt', 'w')
    # file.write(f"This is file {chr(i)}.txt")
    file.close()

# for i in range(65, 91):
#     with open(f"{chr(i)}.txt", 'w') as file:
#         pass
        

# # script to delete the created files
# for i in range(65, 91):
#     os.remove(chr(i)+'.txt')