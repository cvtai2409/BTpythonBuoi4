print("Xoa bo ki tu")
x=0
def xoabokitu(line):
    n=line[:x]+line[x+1:]
    print(n)
line =input("Nhap chuoi: ") 
x=int(input("Nhap vi tri xoa: "))
xoabokitu(line)

