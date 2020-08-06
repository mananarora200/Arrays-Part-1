import os
os.system("cls")
while 1:
    num_array = []
    flag = 0
    count = int(input("Enter number of elements :"))
    for i in range(count):
        num_array.append(int(input(f"Enter {i+1} element :")))
    print(num_array)
    for i,j in enumerate(num_array):
        try:    
            if j == num_array[i+1]:
                flag = 1
                break
        except:
            continue
    if flag == 1:
        print("There is an repeated element in this array")
    else:
        print("There is no repeated element in this array")
    input("Press any key to continue ...")
    os.system("cls")