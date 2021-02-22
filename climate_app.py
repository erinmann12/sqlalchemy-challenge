#import dependencies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import datetime as dt

from flask import Flask, jsonify, request

#--------------------------
#Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect existing database into new model
Base = automap_base()
# Reflect tables
Base.prepare(engine,reflect = True)
# Save references to tables
Measurement = Base.classes.measurement
Station = Base.classes.station

#-----------------------------
# Flast Setup
app = Flask(__name__)

#-----------------------------
# Flask Routes
@app.route("/")
def home():
    """List all available api routes."""
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/start-date <br/>"
        f"/api/v1.0/start-date/end-date"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create session from Python to DB
    session = Session(engine)

    """Return list of precipitation data"""
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation_results = session.query(Measurement.date, func.max(Measurement.prcp)).filter(Measurement.date > query_date)\
        .group_by(Measurement.date).order_by(Measurement.date).all()

    session.close()

    # Create dictionary and append to list presipitation_data
    precipitation_data = []
    for date, prcp in precipitation_results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        precipitation_data.append(precipitation_dict)

    return jsonify(precipitation_data) 

@app.route("/api/v1.0/stations")
def stations():
    # Create session link
    session = Session(engine)

    """Return list of station names"""
    # Query stations
    station_results = session.query(Station.station).all()

    session.close()

    #convert to list
    all_stations = list(np.ravel(station_results))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create session link
    session = Session(engine)

    """Return list of temperature observations for the previous year for most active station"""
    #Query to get most active station
    top_station = session.query(Measurement.station, func.count(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).first()
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #Query to get dates and tobs for most active station
    station_results = session.query(Measurement.station,Measurement.date,Measurement.tobs)\
    .filter(Measurement.station == top_station[0]).filter(Measurement.date > query_date)\
    .order_by(Measurement.date).all()

    session.close()

    # convert into list
    tobs_data = list(np.ravel(station_results))

    return jsonify(tobs_data)

@app.route("/api/v1.0/<date>")
def start(date):
    #Create session 
    session = Session(engine)

    #create datetime object for start date
    start_date = dt.datetime.strptime(date, "%Y-%m-%d")
    
    #query all dates
    start_date_results = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
        .filter(Measurement.date >= start_date).all()

    session.close()

    #convert results into list
    start_date_data = list(np.ravel(start_date_results))

    return jsonify(start_date_data)

@app.route("/api/v1.0/<start>/<end>")
def startend(start,end):
    #Create session 
    session = Session(engine)

    #create datetime object for start date
    start_date = dt.datetime.strptime(start, "%Y-%m-%d")
    end_date = dt.datetime.strptiime(end, "%Y-%m-%d")
    
    #query all dates
    date__range_results = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
        .filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

    session.close()

    #convert results into list
    date_range_data = list(np.ravel(date_range_results))

    return jsonify(date_range_data)


if __name__ == '__main__':
    app.run(debug=True)