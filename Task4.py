import csv

###
def file_writer(student_info):
    with open("School Administration.csv","a",newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Class", "Gender", "Age", "DateofBirth", "PhoneNumber"])
            
        writer.writerow(student_info)
        
###
def writer():
    condition = True
    while(condition):

        student_info = input("Enter the students information in the following format (Name Class Gender(M/F) Age DateofBirth PhoneNumber): ")
        student_info_list = student_info.split(" ")
        print("Entered information is \nName: {}\nClass: {}\nGender: {}\nAge: {}\nDate of Birth: {}\nPhone Number: {}"
             .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3],student_info_list[4],
                    student_info_list[5]))
        
        condition2 = True
        while(condition2):
            info_check = input("Is the entered information correct?(Yes/No)")

            if(info_check.lower() == "yes"):
                file_writer(student_info_list)
                
                condition3 = True
                while(condition3):
                    enter_more_student = input("Do you want enter add another student information?(Yes/No)")
                    if(enter_more_student.lower() == "yes"):
                        condition = True
                        condition3 = False
                    elif (enter_more_student.lower() == "no"):
                        condition = False
                        condition3 = False
                    else:
                        print("Oops! incorrect input")
                    
                condition2 = False

            elif(info_check.lower() == "no"):
                print("Re enter students information!")
                condition2 = False

            else:
                print("Oops! incorrect input")
                
###
def file_reader(dicta):
    with open("School Administration.csv","r",newline='') as csv_file:
        reader = csv.reader(csv_file)
        
        for row in reader:
            header_list = row
            break
        
        temp = 0
        key = []
        value = []
        for i in header_list:
            j = dicta.keys()
            l = dicta.values()
            for k in j:
                if (i.lower() == k.lower()):
                    key.append(temp)
                    value.append(dicta[k])
            temp += 1
            
        #print(key)
        #print(value)
        for row in reader:
            m = 0
            for l in key:
                if (row[l] == value[m]):
                    print(row)
                m += 1
                
###
def input_to_reader():
    condition4 = True
    while(condition4):
        templist = ["name", "class", "gender", "age", "dateofbirth", "phonenumber"]
        tempkey = input("Enter the Key?(Name/Class/Gender/Age/DateOfBirth/PhoneNumber) ")
        if tempkey.lower() in templist:
            print("Nice")
            condition4 = False
            
            tempvalue = input(tempkey+": ")
            return {tempkey:tempvalue}
        else:
            print("Oops! incorrect input")

def reader():
    tempdict = dict()
    condition5 = True
    while(condition5):
        temph = input_to_reader()
        lists1 = list(temph.keys())
        lists2 = list(temph.values())
        tempdict[lists1[0]] = lists2[0]
        
        condition6 = True
        while(condition6):
            abc = input("Do you add more data?(Yes/No) ")
            if (abc.lower() == "yes"):
                condition5 = True
                condition6 = False
            elif (abc.lower() == "no"):
                condition5 = False
                condition6 = False
            else:
                print("Oops! incorrect input")
        
    file_reader(tempdict)
    
###
def main_fun():
    condition1 = True
    while(condition1):
        read_write = input("Do you add member or read member?(add/read)")

        if(read_write.lower() == "add"):
            writer()
            condition1 = False

        elif(read_write.lower() == "read"):
            reader()
            condition1 = False

        else:
            print("Oops! incorrect input")
            condition1 = True
            
###
main_fun()
