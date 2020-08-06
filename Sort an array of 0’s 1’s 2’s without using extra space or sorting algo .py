import os
os.system("cls")
def find(num_array):
    a,b,c = num_array.count(0),num_array.count(1),num_array.count(2)
    print([0 for i in range(a)]+[1 for i in range(b)]+[2 for i in range(c)])
while 1:
    num_array = []
    print("The numbers should be 0, 1 and 2")
    count = int(input("Enter number of elements :"))
    for i in range(count):
        num_array.append(int(input(f"Enter {i+1} element :")))
    find(num_array)
    input("Press any key to continue ...")
    os.system("cls")