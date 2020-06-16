from flask import Flask
from pymongo import MongoClient, DESCENDING, ASCENDING

app = Flask(__name__)

c = MongoClient(host="localhost", port=27017)
dbh = c["traveldb"]


def savetraveldata(travel):
    travel_ = {
        "cardsnumber": travel.carsnumber,
        "from": travel.from_,
        "where": travel.where,
        "date": travel.date,
        "km": travel.km
    }

    dbh.Travels.insert_one(travel_)


def allfilm():
    travels = dbh.Travels.find({})
    t = []
    for travel in travels:
        t.append(travel)

    return t
