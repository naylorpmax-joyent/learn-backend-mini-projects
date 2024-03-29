import sqlite3
import sys


class DB:
    def __init__(self, db_file_path):
        try:
            self.conn = sqlite3.connect(db_file_path)
        except Exception as err:
            print(f"error connecting to local database at {db_file_path}: {err}")
            sys.exit()

    def get_song_location(self, artist, song, track, version):
        """ Retrieve the remote location of a given file """
        
        # TODO: prepare query and arguments
        sql = ""
        args = ()

        return self.select(sql, args)

    def list_songs_by_artist(self, artist):
        """ List the songs and versions of a given artist """

        # TODO: prepare query and arguments
        sql = ""
        args = ()

        return self.select(sql, args)

    def list_songs_by_artist_and_song(self, artist, song):
        """ List the songs and versions of a given artist and song """

        # TODO: prepare query and arguments
        sql = ""
        args = ()

        return self.select(sql, args)

    def store_song_location(self, artist, song, track, version):
        """ Store the remote location of a given track version """
        
        # TODO: prepare query and arguments
        sql = ""
        args = ()

        return self.execute(sql, args)

    def select(self, sql, args):
        """ Helper method to execute statements that return data i.e. SELECTs """
        # create a cursor object
        cursor = self.conn.cursor()

        # execute query
        try:
            cursor.execute(query, args)
        except Exception as err:
            print(err)
            sys.exit()

        # fetch and return the query results
        return cursor.fetchall()

    def execute(self, sql, args):
        """ Helper method to execute statements that do not return any rows """
        # create a cursor object
        cursor = self.conn.cursor()

        # execute query
        try:
            cursor.execute(query, args)
        except Exception as err:
            print(err)
            sys.exit()
