# import dependencies we need to query a sqlite databse with sqlalchemy and return output to flask as json's

import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:////Users/danvaldes/Desktop/Project 3/cricket.sqlite")

# reflect an existing database into a new model
Base = automap_base()

Base.prepare(engine, reflect=True)

Batters = Base.classes.Batters

session = Session(engine)

# FLASK APP INITIALIZED
app = Flask(__name__)

@app.route("/")
def Home():
    return(
        f"<h3>Available Routes:<hr></h3>"
        f"/api/Most Runs</br>"
        f"/api/Hundreds</br>"
        f"/api/Longest Career"
        )

@app.route("/api/Most Runs")
def MostRuns():


@app.route("/api/Longest Career")
def LongestCareer():


@app.route("/api/Hundreds")
def Hundreds():



if __name__ == "__main__":
    app.run(debug=True)