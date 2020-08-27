from app import app
from flask import request, session, redirect, render_template

@app.route("/htmlTutorial")
def htmlTutoral():
    session["lessonNum"] = 1
    session["example"] = "<!DOCTYPE html>\n<html>\n\n<head>\n</head>\n\n<body>\n</body>\n\n</html>"
    return render_template("htmlTutorial.html")


@app.route("/cssTutorial")
def cssTutorial():
    session["cssLessonNum"] = 1
    session["example"] = "<!DOCTYPE html>\n<html>\n\n<head>\n</head>\n\n<body>\n</body>\n\n</html>"
    return render_template("cssTutorial.html")


@app.route("/cssLessons")
def cssLessons():
    if 'cssLessonNum' not in session:
        session["cssLessonNum"] = 1
    num = request.args.get("num")
    if num == "p":
        session["cssLessonNum"] -= 1
    elif num == "n":
        session["cssLessonNum"] += 1
    elif type(num) == str and num.isnumeric:
        session["cssLessonNum"] = int(num)
        return render_template("CSSlesson" + str(session["cssLessonNum"]) + ".html")
    return redirect("/cssLessons?num=" + str(session["cssLessonNum"]))


@app.route("/lessons")
def lessons():
    if 'lessonNum' not in session:
        session["lessonNum"] = 1
    num = request.args.get("num")
    if num == "p":
        session["lessonNum"] -= 1
    elif num == "n":
        session["lessonNum"] += 1
    elif type(num) == str and num.isnumeric:
        session["lessonNum"] = int(num)
        return render_template("lesson" + str(session["lessonNum"]) + ".html")
    return redirect("/lessons?num=" + str(session["lessonNum"]))


@app.route("/exampleEditor", methods=["GET", "PUT"])
def exampleEditor():
    if request.method == "PUT":
        session["example"] = request.json["html"]
        return "Done"
    elif request.method == "GET":
        return render_template("exampleEditor.html", codeDefault=session["example"])
    

@app.route("/formdata", methods=["GET", "POST"])
def formdata():
    data = dict(request.form)
    string = "<br>"
    for key in data:
        string += ("<br>" + key + "=" + str(data[key]) + "<br>")
    return "Your form was received as: " + string