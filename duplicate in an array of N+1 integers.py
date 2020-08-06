import os
os.system("cls")
def find(num_array):
    num_array = sorted(num_array)
    for i,j in enumerate(num_array):
        try:    
            if j == num_array[i+1]:
                return print(f"Repeated element is {j}")
        except:
            continue
    return print("There is no repeated element found in this array")
while 1:
    num_array = []
    count = int(input("Enter number of elements :"))
    for i in range(count):
        num_array.append(int(input(f"Enter {i+1} element :")))
    find(num_array)
    input("Press any key to continue ...")
    os.system("cls")