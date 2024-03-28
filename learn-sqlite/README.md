# learn-sqlite

## Goals

- Get a SQLite database setup locally
- Write some SQL statements
- Write some Python CLI (command line interface) commands that allow users to run specific SQL statements against the database

## Setup

- Download sample database [here](https://www.sqlitetutorial.net/sqlite-sample-database/) and save it as `learn-sqlite/resources/chinook.db`
- Install [Python](https://www.python.org/downloads/) if you haven't done so already
- Create a virtual environment named `sqlite_venv` (or whatever you'd like to call it)

```bash
python3 -m venv sqlite_venv
```

- Activate the virtual environment:

```bash
# Windows - in cmd.exe
sqlite_venv\Scripts\activate.bat

# Windows - in PowerShell
sqlite_venv\Scripts\Activate.ps1

Linux/Mac
source sqlite_venv/bin/activate
```

- Install the project's Python dependencies

```bash
pip install -r requirements.txt
```

- Give it a whirl! Here are some example commands to get you started. These examples assume you to be in this directory / folder.

**Display usage message**

```bash
python src/sqlite.py
```

> ```bash
> Usage: sqlite.py [OPTIONS] COMMAND [ARGS]...
>
> Options:
>  --help  Show this message and exit.
>
> Commands:
>  tracks  Pass an artist name to search the database for their tracks
> ```

**Search for tracks by an artist in the database**

```bash
python src/sqlite.py tracks --artist "Jimi Hendrix"
```

> ```bash
> Connecting to local database at: resources/chinook.db
> Successfully connected to database (v2.6.0)
> Found 17 tracks by Jimi Hendrix
> * Foxy Lady (from: Are You Experienced?)
> * Manic Depression (from: Are You Experienced?)
> * Red House (from: Are You Experienced?)
> * Can You See Me (from: Are You Experienced?)
> * Love Or Confusion (from: Are You Experienced?)
> * I Don't Live Today (from: Are You Experienced?)
> * May This Be Love (from: Are You Experienced?)
> * Fire (from: Are You Experienced?)
> * Third Stone From The Sun (from: Are You Experienced?)
> * Remember (from: Are You Experienced?)
> * Are You Experienced? (from: Are You Experienced?)
> * Hey Joe (from: Are You Experienced?)
> * Stone Free (from: Are You Experienced?)
> * Purple Haze (from: Are You Experienced?)
> * 51st Anniversary (from: Are You Experienced?)
> * The Wind Cries Mary (from: Are You Experienced?)
> * Highway Chile (from: Are You Experienced?)
> ```

**Search for tracks by an artist that is NOT in the database**

```bash
python src/sqlite.py tracks --artist "Taylor Swift"
```

> ```bash
> Connecting to local database at: resources/chinook.db
> Successfully connected to database (v2.6.0)
> No tracks found by Taylor Swift - must be too obscure!
> ```

## Challenges

### Explore the database

You can use UI software or the command line / terminal to explore the database. UI tools will allow you to visualize the data more easily - [Beekeeper](https://www.beekeeperstudio.io/) is my favourite for Mac, [DBeaver](https://dbeaver.com/docs/dbeaver/Database-driver-SQLite/) is a popular tool for Windows.

To explore the database via the command line instead, the SQLite CLI comes pre-installed the Terminal on Mac; on Windows, you can [install SQLite](https://www.servermania.com/kb/articles/install-sqlite). To open the database, simply run `sqlite3 <path_to_a_local_database_file>` - for example:

```bash
sqlite3 resources/chinook.db
```

The SQLite Tutorial site also provides a diagram showing the sample database's schema to help you get started [here](https://www.sqlitetutorial.net/sqlite-sample-database/).

### Write new queries

Once you've got some ideas of how your tool's users might want to query or interact with this data, try designing and writing some queries, and testing/tweaking them until they do what you want.

Here are a bunch of ideas / questions to get you started - pick any that seem interesting to you, brainstorm others, or start with just one!

**Reads**

*See [this resource](https://www.sqlitetutorial.net/sqlite-select/) to learn how to select/read data from a SQLite database - most of the syntax is standard across other SQL flavours too!*

- How many customers listen to a given artist?
- Top X tracks/artists by the most revenue?
- Top X tracks/artists by popularity?

**Writes**

*See [this resource](https://www.sqlitetutorial.net/sqlite-insert/) to learn how to insert/write data to a SQLite database - most of the syntax is standard across other SQL flavours too!*

- Add a new genre
- Add a new artist, along with their tracks (maybe from a CSV file? :eyes:)
- Change the genre of a track

- Add a new customer
- Add a new invoice for a given customer
- Add new items to a given invoice

### Add new commands to the CLI

After writing a query you'd like to add to your tool, update the CLI tool to support the new query. Think about the information the user will need to provide, which are required vs optional, and what might make it easier for them.

For example, if you want to support any write queries where the user may need to provide a LOT of information (either more than a handful of columns or more than a handful of rows), instead of running a lot of commands, perhaps you could let them provide the path to a CSV file instead of each datapoint as a separate argument.

## Resources

- [Virtual environments in Python](https://python.land/virtual-environments/virtualenv)
- [Click](https://click.palletsprojects.com/en/8.1.x/) - Python library for creating CLI tools
