# sqlalchemy-challenge

#You are asked to analyze climate data using sqlalchemy and design a climate app with static and dynamic API routes based on the following instructions 

## Instructions:

##Connect to the database "hawaii.sqlite", reflect the tables into classes, save references to variables, create and SQLAlchemy session to connect to the database. 

Precipitation Analysis 

## Get precipitation data for one year from the most recent data in the dataset, load the results into a Pandas dataframe and plot the results using the pd plot method, print summary statistics for the dataframe. 

Station Analysis 

## Calculate the total number of stations in the dataset, find the most active stations, get the minimum, maximum and average temperatures for the most active station id.

Temperature Analysis

##Get the temperature observation data for the previous 12 months for the most active station. Make a histogram based on the results using 12 bins. 

Climate App 

## Define a function for your homepage and list all the available routes on your homepage using Flask. 

Routes 

#/api/v1.0/precipitation 

# Return a json dictionary of the query results from your precipitation analysis. Set the date as the key and prcp as the value

#/api/v1.0/stations

# Return a json list of all the stations in the dataset 

#/api/v1.0/tobs

# Return a json list of temperature observations for the previous year for the most active station in the dataset

#/api/v1.0/<start> and /api/v1.0/<start>/<end>

# Return a json list of the lowest, highest and maximum temperatures for a start date and start-end range to be specified by the user. 

 