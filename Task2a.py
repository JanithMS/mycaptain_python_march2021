#Write a Python Program for Fibonacci numbers.

a = [0]
a.append(1)
for i in range (1,12):
    a.append(a[i] + a[i-1])
    
print(a)
