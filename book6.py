print("Doi kieu chu")
def doichu(line):
    x = ""
    for i in line:
        if i.islower():
            x+=i.upper()
        else:
            x+=i.lower()
    print(x)
line=input("Nhap chuoi: ")
doichu(line)

