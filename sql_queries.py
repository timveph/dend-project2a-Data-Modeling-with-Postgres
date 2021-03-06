# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = ("""create table if not exists songplays \
                            (songplay_id serial, start_time timestamp NOT NULL, user_id varchar NOT NULL \
                            , level varchar, song_id varchar NOT NULL, artist_id varchar NOT NULL \
                            , session_id varchar NOT NULL, location varchar, user_agent varchar \
                            , PRIMARY KEY (user_id, song_id, artist_id))""")

user_table_create = ("""create table if not exists users \
                        (user_id varchar PRIMARY KEY NOT NULL, first_name varchar, last_name varchar, gender char \
                        , level varchar)""")

song_table_create = ("""create table if not exists songs \
                        (song_id varchar PRIMARY KEY NOT NULL, title varchar, artist_id varchar NOT NULL \
                        , year int, duration float4)""")

artist_table_create = ("""create table if not exists artists \
                        (artist_id varchar PRIMARY KEY NOT NULL, artist_name varchar, artist_location varchar \
                        , artist_latitude varchar, artist_longitude varchar)""")

                     #how do I store this data?
time_table_create = ("""create table if not exists time \
                        (start_time timestamp NOT NULL, hour int, day int, week int, month int\
                        ,year int, weekday varchar)""")

# INSERT RECORDS

songplay_table_insert = ("""insert into songplays \
                            (songplay_id, start_time, user_id, level, song_id, artist_id, session_id \
                            ,location, user_agent) \
                             values (%s, %s, %s, %s, %s, %s, %s, %s, %s) \
                             ON CONFLICT(user_id, song_id, artist_id) \
                             DO NOTHING""")

user_table_insert = ("""insert into users \
                            (user_id, first_name, last_name, gender, level) \
                            values (%s, %s, %s, %s, %s) \
                            ON CONFLICT (user_id) \
                            DO UPDATE \
                                SET level  = EXCLUDED.level\
                        ;""")
# user_table_insert = ("""insert into users \
#                             (user_id, first_name, last_name, gender, level) \
#                             values (%s, %s, %s, %s, %s) \
#                         ;""")

song_table_insert = ("""insert into songs \
                            (song_id, title, artist_id, year, duration) \
                            values (%s, %s, %s, %s, %s)""")

artist_table_insert = ("""insert into artists \
                            (artist_id, artist_name, artist_location, artist_latitude, artist_longitude) \
                            values (%s, %s, %s, %s, %s) \
                            ON CONFLICT (artist_id) \
                            DO NOTHING""")

time_table_insert = ("""insert into time \
                            (start_time, hour, day, week, month, year, weekday) \
                            values (%s, %s, %s, %s, %s, %s, %s)""")


# # FIND SONGS

song_select = ("""select s.song_id, a.artist_id \
                    from  songs s, artists a\
                    where s.artist_id = a.artist_id""")


# QUERY LISTS
# create_table_queries = [songplay_table_create]
create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]