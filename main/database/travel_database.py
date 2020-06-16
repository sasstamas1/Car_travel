from flask import Flask
from pymongo import MongoClient, DESCENDING, ASCENDING

app = Flask(__name__)

c = MongoClient(host="localhost", port=27017)
dbh = c["traveldb"]


def savetraveldata(travel):
    travel_ = {
        "carsnumber": travel.carsnumber,
        "from": travel.from_,
        "where": travel.where,
        "date": travel.date,
        "km": travel.km,
        "fuel": travel.fuel
    }

    dbh.Travels.insert_one(travel_)


def alltravel():
    travels = dbh.Travels.find({})
    t = []
    for travel in travels:
        t.append(travel)
    return t


def findtravels_bycarsnumberanddate(carsnumber, begindate, enddate):
    travels = dbh.Travels.find({'carsnumber': carsnumber})
    t = []
    for travel in travels:
        if begindate <= travel['date'] <= enddate:
            t.append(travel)
    return t
