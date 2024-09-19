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
engine = create_engine("sqlite:///hawaii.sqlite")

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
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    #Create a query that finds the most recent date in the dataset (8/23/2017)

    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= query_date).all()
    
    # Calculate the date one year from the last date in data set.
    
    query_date_flask = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    results_flask = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= query_date_flask).all()

    session.close()

    precipitation_results = []
    for date,prcp in results_flask:
        precipitation_dict = {}







if __name__ == '__main__':
    app.run(debug=True)
