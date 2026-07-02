age = int(input("How old are you?\n"))
if age > 0:
    print(f"You are {age//10} decades and {age%10} \nyear(s) old.")
else:
    print("Please enter a valid age.")