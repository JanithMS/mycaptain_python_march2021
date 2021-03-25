#Write a Python program to print all positive numbers in a range.

inputdata = input("list1= ")
list1 = inputdata.split(',')
listpositive = []
for a in list1:
    if int(a) >= 0:
        listpositive.append(int(a))
        
print("Output: " + str(listpositive))
