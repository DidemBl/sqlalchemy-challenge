# Import the dependencies.
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import func
from flask import Flask, jsonify



#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB

session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes

#################################################
#Homepage
@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    #Create a query that finds the most recent date in the dataset (8/23/2017)

    query_date_flask = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= query_date_flask).all()
    
    # Calculate the date one year from the last date in data set.
    
   

    results_flask = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= query_date_flask).all()

    session.close()

    precipitation_results = []
    for date,prcp in results_flask:
        precipitation_dict = {}
        precipitation_dict[date] = prcp
        precipitation_results.append(precipitation_dict)
    return jsonify(precipitation_results)

@app.route("/api/v1.0/stations")
def stations():

     # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all the stations in the dataset 

    results_station_flask = session.query(Station.station).all()

    session.close()

    all_stations=list(np.ravel(results_station_flask))

    return jsonify(all_stations) 

@app.route("/api/v1.0/tobs")
def tobs():

     # Create our session (link) from Python to the DB
    session = Session(engine)

    #Query the dates and temperature observations of the most-active station for the previous year of data.

    active_latest = session.query( Measurement.date).\
    filter(Measurement.station == "USC00519281").\
    order_by((Measurement.date).desc()).first()
    
    query_date_active_flask= dt.date(2017, 8, 18) - dt.timedelta(days=365)
    
    results_active_flask = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.date >= query_date_active_flask).\
    filter(Measurement.station == "USC00519281").all()

    session.close()

    tobs_results=[]
    for date,tobs in results_active_flask:
        tobs_dict = {}
        tobs_dict[date] = tobs
        tobs_results.append(tobs_dict)

    return jsonify(tobs_results)

@app.route("/api/v1.0/<start>")
def start_date(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    #Query the database for max, min and avg temperatures
    """Fetch the temperature info for the start date that matches the path variable supplied by the user, or a 404 if not.
       the path variable supplied by the user, or a 404 if not."""


    results_start = [Measurement.date,
       func.max(Measurement.tobs),
       func.min(Measurement.tobs),
       func.avg(Measurement.tobs)]
    results_query = session.query(*results_start).\
    filter(Measurement.date >= start).all()

    session.close()
    #Make a dictionary using the query results

    results_start_dict = list(np.ravel(results_query))

    return jsonify(results_start_dict)


if __name__ == '__main__':
    app.run(debug=True)
