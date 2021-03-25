#write a Python program which accepts the radius of a circle from the user and computes area.

radius = float(input("Input the radius of circle: "))
area = (22*radius*radius)/7
print("The area of the circle with radius {} is: {}".format(radius, area))

#write a Python program to accept a filename from the user and print the extension of that.

filename = input("Input the Filename: ")
extension = filename.split(".")
print ("The extension of the file is : " + extension[-1])
