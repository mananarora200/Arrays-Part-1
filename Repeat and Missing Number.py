import os
os.system("cls")
def find(num_array):
    num_array = sorted(num_array)
    num_list = [i+1 for i in range(len(num_array))]
    rpt = []
    missing_list = []
    for i in num_list:
        if i not in num_array:
            missing_list.append(i)
    for i,j in enumerate(num_array):
        try:
            if j == num_array[i+1]:
                rpt.append(j)
        except:
            continue
    print(f"Missing elements are {missing_list}",end="")
    print(f"\t Repeated element are {rpt}")


while 1:
    num_array = []
    print("The numbers should between 1 and  length of the array")
    count = int(input("Enter number of elements :"))
    for i in range(count):
        num_array.append(int(input(f"Enter {i+1} element :")))
    find(num_array)
    input("Press any key to continue ...")
    os.system("cls")