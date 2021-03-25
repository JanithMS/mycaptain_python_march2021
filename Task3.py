#Write Python code to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Use dictionaries.

# function for printing frequency in desending order
def fun2(mydict):
    def fun1(mydict):
        for k in mydict:
            if mydict[k] == max(mydict.values()):
                p = str(k)+" = "+str("{0:0=2d}".format(mydict[k]))+" "
                mydict.pop(k)
                return p

    m = len(mydict)
    x = ""
    for l in range(m):
        x = x + fun1(mydict)

    return x
  
inputstring = input("Please enter a string: ")
def most_frequent(a):
    a = a.lower()
    b = dict()
    for i in set(a):
        n = 0
        for j in list(a):
            if i == j:
                n += 1

        b[i] = n
        
    return fun2(b)
    
print(most_frequent(inputstring))
