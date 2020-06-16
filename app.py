from flask import Flask, render_template, request

from main.model.travel import Travel
from main.database.travel_database import savetraveldata

app = Flask(__name__)


@app.route('/')
@app.route('/inputdata')
def inputpage():
    return render_template("input.html")


@app.route('/outputdata')
def outputpage():
    return render_template("output.html")


@app.route('/savedata', methods=['POST'])
def savenewdata():
    if (request.form['carsnumber'] is not "" or
            request.form['from'] is not "" or
            request.form['where'] is not "" or
            request.form['date'] is not "" or
            request.form['km'] is not ""):
        travel = Travel(request.form['carsnumber'], request.form['from'], request.form['where'], request.form['date'],
                        request.form['km'])
        savetraveldata(travel)
    return render_template("input.html")


if __name__ == '__main__':
    app.run()
