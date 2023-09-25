def greeting( str ):
    print(str)
    return

greeting("Hello !")
greeting("Please enter your identity.")

name=str(input("Your name: "))
address=str(input("Enter your address: "))
sex=str(input("Type 'M' for Male and 'F' for Female: "))

f = open("personal_info.txt", "w")
f.write(name)
f.write(address)
f.write(sex)
f.close()

def info():
    print("Your name is registered.")
    return
info()

f = open("personal_info.txt", "r")
print(f.read())
