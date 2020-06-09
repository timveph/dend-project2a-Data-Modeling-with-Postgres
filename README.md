# Sparkify
## How the data is modelled



### Technical information
*Database:* PostGres

*Platform:* AWS

*Programming Language:* Python and SQL

*Process:* ETL




### The Business Case
Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. 
The analytics team is particularly interested in understanding what songs users are listening to.



### A diagram of how the data is modelled
#### Type: Star Schema
![Star Schema: Sparkify ERD](https://github.com/timveph/dend-project2a-Data-Modeling-with-Postgres/blob/master/sparkify%20ERD.jpg)

> Each key is captured as a varchar. As there is no requirement to do any aggregation on keys, the design team felt that varchar was suitable. 

> _(I am basing this on past experience within databases) This also saves harddrive space and avoids issues later on when the key's value might become to big to fit inside of an int._


#### Table: songplay

***Type***: Fact

***Primary Key:*** Is a composite key made up of:

* user_id
* song_id
* artist_id

This table contains records in log data associated with song plays.



#### Table: users

***Type***: Dimension

***Primary Key:*** user_id

This table contains information about the users who use the Sparkify app.



#### Table: artists

***Type***: Dimension

***Primary Key:*** artist_id

This table contains information about the artists whose songs are played by users via the app.



#### Table: songs

***Type***: Dimension

**Primary Key:*** song_id

This table contains the title of the song, year it was released, how long it is and who the artist is. 



#### Table: songs

***Type***: Dimension

This table contains the timestamps of records in songplays broken down into specific units.


### Why this design


* A star schema was chosen to facility fast queries using SQL. 
    * Allow for complex analytical and ad hoc queries, including aggregations
* The data structure has also been denormolised to make it informative for the users. 
* Allows for additional data to be added at a later date if required


### The ETL process
To load the data with data for the first time please follow the following steps:
> ***Please note:*** The "sql_queries.py" file is central to the process. It contains the drop, create, insert and sql queries that are used within the ETL process. Care must be taken when editing these files as the integrity of the data tables can be compromised.


1. run the "create_tables.py" file in the python terminal
> This process will create the tables needed to capture the data from the song and log files

    > Please note, it will drop/delete any of the tables (and their data) if it exists

2. run the "etl.py" file in the python terminal window
> This process will read each song and log file and copy the content into the data tables. 

    > If you want to check the data tables have content, please open and run the code in the Jupyter Notebook "test.ipynb"



### Example queries
With the star schema you can quickly and easily query the data for a variety of stats to do with how users are using the app. For example:

> _Not, these queries are run within AWS Jupyter Notebook_

---

**Query 1 Example**

`%sql SELECT COUNT(songplay_id) as plays, level 
    from songplays 
    group by level`
    
**Output**

![Query 1 Example](https://github.com/timveph/dend-project2a-Data-Modeling-with-Postgres/blob/master/query1example.JPG "Query 1 Example")

---

**Query 2 Example**

`%sql select s.title, a.artist_name, count(sp.*) as plays 
        from (songplays sp 
                join songs s 
                on sp.song_id=s.song_id) 
            join artists a 
                on sp.artist_id=a.artist_id 
        group by title, artist_name
`

**Output**

![Query 2 Example](https://github.com/timveph/dend-project2a-Data-Modeling-with-Postgres/blob/master/query2example.JPG "Query 2 Example")
