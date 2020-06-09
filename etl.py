import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *    

# conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")


def process_song_file(cur, filepath):
    # open song file
#     df = pd.read_json(filepath,lines=True)
#     df = process_data(cur, conn, filepath, func=process_song_file)
    df = pd.read_json(filepath,lines=True)

    # insert song record
    song_data = list(df[['song_id','title','artist_id','year','duration']].values[0])
    
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = list(df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude' , 'artist_longitude']].values[0])
                    

    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    # open log file
#     df = process_data(cur, conn, filepath, func=process_log_file) 
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page']=='NextSong']

    # convert timestamp column to datetime
    df['ts'] = pd.to_datetime(df['ts'], unit='ms')
    
    # insert time data records
#     time_data = 
#     column_labels = 
#     time_df = 
    timestamp = df['ts']
    hour = timestamp.dt.hour.values
    day = timestamp.dt.day.values
    woy = timestamp.dt.weekofyear.values
    month = timestamp.dt.month.values
    year = timestamp.dt.year.values
    weekday = timestamp.dt.weekday.values
    
    time_df = pd.DataFrame({'TIMESTAMP':timestamp,'HOUR':hour,'DAY':day,'WEEKOFYEAR':woy,'MONTH':month,'YEAR':year,'WEEKDAY':weekday})


    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId','firstName','lastName','gender','level']].copy()
    user_df.columns = ['user_id','first_name','last_name','gender','level']

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            song_id, artist_id = results
        else:
            song_id, artist_id = None, None

        # insert songplay record
        songplay_data = (index, pd.to_datetime(row.ts, unit='ms'), row.userId, row.level, song_id, artist_id, row.sessionId, row.location, row.userAgent)
#         songplay_data = (index, row.ts, row.user_id, row.level, song_id, artist_id, row.sessionId, row.location, row.user_agent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()