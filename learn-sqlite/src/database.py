import sqlite3
import sys


def connect(db_file_path):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file_path)
        print(f"Successfully connected to database (v{sqlite3.version})")
    except Exception as err:
        print(f"error connecting to local database at {db_file_path}: {err}")
        sys.exit()

    return conn


def select_tracks_by_artist(conn, artist_name):
    """ query for tracks by the given artist """
    
    # prepare query and arguments
    query = """
        SELECT
            tracks.Name,
            albums.Title
        FROM
            tracks
            LEFT JOIN albums ON albums.AlbumId = tracks.AlbumId
            LEFT JOIN artists ON artists.ArtistId = albums.ArtistId
        WHERE
            artists.Name = ?
    """
    args = (artist_name,)

    # create a cursor object
    cur = conn.cursor()

    # execute query
    try:
        cur.execute(query, args)
    except Exception as err:
        print(err)
        sys.exit()

    # fetch and return the query results
    return cur.fetchall()
