from flask import Flask, render_template, json, request, redirect, session, url_for
app = Flask(__name__)

studentlist = []
response = []

filename = "student.txt"

@app.route('/',methods=["GET", "POST"])
def main():

    try:
        del studentlist[:]
        count = 0
        inpfile = open(filename,"r")
        for str in inpfile:
            studentlist.append(str)
            count = count + 1
        if count == 0:
            response.append("Class is empty")
        inpfile.close()
    except:
        response.append("Class does not exists")

    
    return render_template('cox.html',studentlist=studentlist,response=response)

@app.route('/addStudent',methods = ['POST', 'GET'])

def addStudent():
    del response[:]
    found = False
    _sname = request.form["sname"]

    if  _sname > " ":

        inpfile = open(filename,"r")
        for str in inpfile:
            if str.rstrip("\n") == _sname:
               found = True
        inpfile.close()

        if found:
            response.append("Student already exists")
        else:
            inpfile = open(filename,"a")
            inpfile.write(_sname + "\n")
            inpfile.close()
            response.append("Student added successfuly")
    else:
        response.append("Please enter student name")


    return redirect("/")

@app.route('/updStudent',methods = ['POST', 'GET'])

def updStudent():

    _oldname = (request.form["oldname"]).rstrip("\r\n")
    _newname = request.form["newname"]
    del response[:]
    del studentlist[:]

    if  _newname > " " and _newname != _oldname:
        inpfile = open(filename,"r")
        for str in inpfile:
            if str.rstrip("\n") == _oldname:
               studentlist.append((_newname + "\n"))
            else:
                studentlist.append(str)

        inpfile.close()
        inpfile = open(filename,"w")
        for str in studentlist:
            inpfile.write(str)
        inpfile.close()
        response.append("Student updated successfuly")
    else:
        response.append("Please enter new student name")

    return redirect("/")

@app.route('/delStudent',methods = ['POST', 'GET'])

def delStudent():

    _name = (request.form["name"]).rstrip("\r\n")
    del studentlist[:]
    del response[:]
    inpfile = open(filename,"r")
    for str in inpfile:
        if str.rstrip("\n") != _name:
            studentlist.append(str)
    inpfile.close()
    inpfile = open(filename,"w")
    for str in studentlist:
        inpfile.write(str)
    inpfile.close()
    response.append("Student deleted successfuly")

    return redirect("/")

if __name__ == "__main__":
    app.run()
