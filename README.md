# sqlalchemy-challenge
**Background**

I was tasked with analyzing climate data in Honolulu, Hawaii, to inform my fictional trip there. 

**Tools Used**

1. Python
2. SQLAlchemy
3. ORM Queries
4. Pandas
5. Matplotlib
6. Flask API

**Project Tasks**

In step one of this project, I was tasked with using Python and SQLAlchemy to do basic analysis and data exploration of a climate database using SQLAlchemy, ORM queries, Pandas, and Matplotlib. This included using SQLAlchemy to connect to the sqlite database and reflecting tables into classes.

![](https://github.com/erinmann12/sqlalchemy-challenge/blob/main/Images/datasample.PNG)

Next I designed a query to retrieve the last 12 months of precipitation data. I loaded the query results into a Pandas DataFrame and sorted the values by date. After the initial analysis was done, I used the DataFrame plot method to plot the precipitation data. I then used Pandas to print the summary statistics. 

![](https://github.com/erinmann12/sqlalchemy-challenge/blob/main/Images/precipitationanalysis.png)

For the station analysis, I designed a query to calculate the total number of stations and to find the most active stations. Next I designed a query to retrieve the last 12 months of temperature observation data and plotted the results in a histogram. 

![](https://github.com/erinmann12/sqlalchemy-challenge/blob/main/Images/tempanalysis.png)

In step two, I was tasked with designing a Flask API based on the queries that were developed in step one. 