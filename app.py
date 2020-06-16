from flask import Flask, render_template, request

from main.model.travel import Travel
from main.database.travel_database import savetraveldata, findtravels_bycarsnumberanddate

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
    if (request.form['carsnumber'] is not "" and request.form['carsnumber'] is not None and
            request.form['from'] is not "" and request.form['from'] is not None and
            request.form['where'] is not "" and request.form['where'] is not None and
            request.form['date'] is not "" and request.form['date'] is not None and
            request.form['km'] is not "" and request.form['km'] is not None and
            request.form['fuel'] is not "" and request.form['fuel'] is not None):
        travel = Travel(request.form['carsnumber'], request.form['from'], request.form['where'], request.form['date'],
                        request.form['km'], request.form['fuel'])
        savetraveldata(travel)
    else:
        error = "Hiányzó adat!"
        return render_template("input.html", error=error)
    return render_template("input.html")


@app.route('/finddata', methods=['POST'])
def findtraveldata():
    print(findtravels_bycarsnumberanddate(request.form['carsnumber'],request.form['begindate'],request.form['enddate']))
    return render_template("output.html")


if __name__ == '__main__':
    app.run()
