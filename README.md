# Data Modeling with Postgres
Using fictitious data from a startup called Sparkify, build an ETL pipeline using Python, creating a Postgres Database and defining the data model. 


## Schema for Song Play Analysis
Using the song and log datasets, you'll need to create a star schema optimized for queries on song play analysis. This includes the following tables.

### Fact Table
**songplays** - records in log data associated with song plays i.e. records with page NextSong  
> **fields** - songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

### Dimension Tables
**users** - users in the app  
> **fields** - user_id, first_name, last_name, gender, level  

**songs** - songs in music database  
> **fields** - song_id, title, artist_id, year, duration  

**artists** - artists in music database  
>**fields** - artist_id, name, location, latitude, longitude  

**time** - timestamps of records in songplays broken down into specific units  
>**fields** - start_time, hour, day, week, month, year, weekday

 
## Project steps
1. Create tables using create statements
2. Build an ETL process in python
