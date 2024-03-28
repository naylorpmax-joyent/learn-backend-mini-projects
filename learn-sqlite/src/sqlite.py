# Python native imports
import os
import sys

# external imports
import click

# local imports (any files under ./src/)
import database


@click.group() # https://click.palletsprojects.com/en/8.1.x/api/#click.group
def root():
    pass


@root.command() # https://click.palletsprojects.com/en/8.1.x/api/#click.command
@click.option("--artist", type=str, required=True)
def tracks(artist):
    """
    Pass an artist name to search the database for their tracks
    """

    """
    This is our first command! Right now, it allows the user to look
    up tracks released by the artist they provided.

    We can make it fancier though... Maybe the user wants to also filter
    their search to a specific album? Maybe they only want to see tracks
    that start with M, or only tracks longer than 3 minutes? :)
    """

    # connect to the database
    conn = connect()

    # query the database for tracks by the artist
    results = database.select_tracks_by_artist(conn, artist)
    if len(results) == 0:
        print(f"No tracks found by {artist} - must be too obscure!")
        return

    # the artist has tracks in the database!
    # we selected two columns in the query: the track title
    # and the album title. let's show the user both columns. 
    print(f"Found {len(results)} tracks by {artist}")
    for row in results:
        track_title = row[0]
        album_title = row[1]
        print(f"* {track_title} (from: {album_title})")


def connect():
    """
    This is a little helper function to connect to the database
    via an environment variable.
   
    Using environment variables gives the user flexibility to
    tell us where the database is, without requiring the user to
    type the location every single time they want to run a command.
    """

    db_file_path = os.getenv("DB_FILE_PATH", "")
    if db_file_path == "":
        print("error: missing DB_FILE_PATH environment variable")
        sys.exit()
    
    print(f"Connecting to local database at: {db_file_path}")
    return database.connect(db_file_path)


if __name__ == "__main__":
    root()
