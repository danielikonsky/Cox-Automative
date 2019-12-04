# GRUD
# HERE GOES CODE TO RETRIVE PARAMETERES FROM GET AND PASS IT TO THE PROGRAM
# CAN BE DONE IN FLASK

request = input("Enter request: ")
studentname = ""
updstudentname = ""
newstudent = ""
result = ""

studentlist = []
filename = "student.txt"

def initial():

    try:
        inpfile = open(filename,"r")
        for str in inpfile:
            studentlist.append(str)
        inpfile.close()
        result = "OK"
    except:
        print("Student File does not exist")
        result = "Student File does not exist"
    return result

def add(newstudent):

    try:
        inpfile = open(filename,"r")
        for str in inpfile:
            studentlist.append(str)
        inpfile.close()
        studentlist.append(newstudent + "\n")
        inpfile = open(filename,"w")
        for str in studentlist:
            inpfile.write(str)
        inpfile.close()
        result = "OK"
    except:
        print("Student File does not exist")
        result = "Student File does not exist"
    return result

def update(studentname,updstudentname):
    try:
        found = False
        inpfile = open(filename,"r")
        for str in inpfile:
            if str.rstrip() == studentname:
               found = True
               studentlist.append(updstudentname + "\n")
            else:
                studentlist.append(str)
        inpfile.close()

        if found == False:
            result = "Student not found"
        else:
            inpfile = open(filename,"w")
            for str in studentlist:
                inpfile.write(str)
            inpfile.close()
            result = "OK"
    except:
        print("Student File does not exist")
        result = "Student File does not exist"
    return result
def delete(studentname):
    try:
        found = False
        inpfile = open(filename,"r")
        for str in inpfile:
            if str.rstrip() == studentname:
               found = True
            else:
                studentlist.append(str)
        inpfile.close()

        if found == False:
            result = "Student not found"
        else:
            inpfile = open(filename,"w")
            for str in studentlist:
                inpfile.write(str)
            inpfile.close()
            result = "OK"
    except:
        print("Student File does not exist")
        result = "Student File does not exist"
    return result

if request == "add":
    newstudent = input("Enter student name: ")
    result = add(newstudent)

elif request == "update":
    studentname = input("Enter student name : ")
    updstudentname = input("Enter new student name : ")
    result = update(studentname,updstudentname)

elif request == "delete":
      studentname = input("Enter student name: ")
      result = delete(studentname)

elif request == "end":
      quit()
elif request == "browse":
      initial()
else:
      print("This is a wrong request")

inpfile = open(filename,"r")
for str in inpfile:
    print (str)
print ("Result of operation : " + result)
