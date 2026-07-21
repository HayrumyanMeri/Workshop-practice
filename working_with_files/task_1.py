with open('myinfo.txt', 'w+') as file:
    file.write("Hello\n")
    file.write("it's my first file handling!")
    file.seek(0)
    print(file.read())
