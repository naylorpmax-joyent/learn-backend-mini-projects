# Relational Databases

## what is it

### Database

A collection of software that is designed to enable you manage the lifecycle of longterm data: 1) create, 2) read, 3) update, and 4) delete (CRUD). Like any digital data, data stored in a database will take up memory and/or disk storage on the computer that hosts the database; and like any digital data, *some* program needs to keep track of which data lives where on the host. Enter the database server!

A database server accepts local or remote requests from database clients to read or write its data; consults its "map" of the host computer's memory/storage; and performs the requested action. Data that lives in a database is intended to be permanent, as opposed to ephemeral, meaning that your data should only go away when you specifically tell the database to delete it (if the database is working correctly at least!).

### Relational database

There are a LOT of different kinds, or "flavours", of databases, but all of them more or less fall into these two categories: *relational/SQL* and *non-relational/NoSQL*. Relational databases are, you guessed it, intended to be used with data that is characterized by its relationships with other data. The power of relational databases is determined primarily by how well your **schema** design (i.e. structure and organization of your data) suits your application's data access patterns.

Relational databases are made up of **tables**, each of which is a matrix of **rows** and **columns** (along with some other optional attributes that we'll get into in a moment). Tables in the same database can be freely used together via their relationships.

Here's a quick mockup of an example database that has two tables, to show how they could be connected.

* The first table is named `albums`, and has these columns:
   * name - name of the album
   * artist - name of the artist that created the album
   * producer - name of the producer for the album
   * release\_date - date the album was released
* And the `songs` table has these columns:
   * title - name of the song
   * album - name of the album that the song belongs to
   * length - length of the song

These two tables are related through a column that exists in both tables (even though it has a different name in each) and conceptually links them together - `name` in the `albums` table, and `album` in the `songs` table. In a real-life database, we would probably also tell the database that `songs.name` is a "foreign key" on `albums.name` (more on that later).

Two simple tables can already let you access so much information. Here are just a few things we could find with these - try to figure out which table you need to find this information, or if you would need to consult both:

* List of songs released in 1975 by Labi Siffre that are longer than 5 minutes
* The number of albums produced by Shawn Everett, by artist. For example:
   * The War on Drugs has released 2 albums produced by Shawn Everett
   * Alvvays has released 1 album produced by Shawn Everett
   * Megan Thee Stallion has released 0 albums produced by Shawn Everett / never worked with him
   * etc.
* Total length of HIT ME HARD AND SOFT by Billie Eilish (notice we don't have a column for album length)

Non-relational / "NoSQL" databases on the other hand are *not* structured around traditional column-row relationships. However, NoSQL is more of an umbrella term, with only a negative definition, since there are lots of different models for non-relational databases - key-value stores, graph databases, and document databases, just to name a few of the most popular types.

If you have the right use case, choosing a NoSQL data model can be immensely efficient and intuitive. However, like any technical decision, it depends on what you're trying to do. In my experience, if your use case has any degree of flux -- even if in the near-future, your usage pattern does seem to align well with a particular NoSQL data model! -- then choosing a relational data model will provide you with the most flexibility, rather than locking you early-on into a particular paradigm.

Relational data models are the vanilla ice cream of the data world: classic and easy to build on as a foundation. And unless your use case is very niche, then with thoughtful table and query design, you may find it difficult to beat relational data models for efficiency and ease-of-use. So let's dive into how these databases work, and how to best take advantage of them - starting with some quick terminology.

### Tables, Rows, and Columns

* A database can have many tables
* A table is made up of a matrix of rows and columns
* At minimum, a column has 1. a name and 2. a datatype
* A row is made up of a single value per column of the correct datatype; that value may be NULL (unless the column doesn't allow NULLs)

### Data Types

* Different SQL database flavours support a different list of datatypes; but they more or less handle the typical datatypes you're likely already familiar with (strings, integers, floats, dates and times, booleans, etc).
* SQL databases typically use a more nuanced, precise approach to datatypes than most programming languages, especially around sizing. For example, rather than a single `string` type, you'll see `VARCHAR`, which can be a sequence of characters up to the maximum length; e.g. `VARCHAR(10)` allocates space to store up to 10 characters.
* This focus on sizing comes from a concern around optimizing operations over what can be become a VERY large amount of data. Using `VARCHAR(1000)` when you know you'll only be storing <10-character strings may not negatively affect performance or allocated storage for a few hundred records; but unnecessarily allocating ~990 bytes for each and every row DOES start to stack up once you're storing millions of rows!

### CAP Theorem

TODO

### Keys

* There are two main types of keys in relational databases - *primary keys* and *foreign keys*
* A key of either type is defined as a set of one or columns on a single table

**Primary keys**

* Here are some of the main things that primary keys do:
   * Enforce uniqueness across rows in a table on the column(s) in the key. No two rows in a table can have the same value(s) in the same column(s) that are part of the primary key.
   * May speed up most operations, such as reads, updates, and joins
   * May slow down some operations, such as inserts and deletes
* A table can only have at most one primary key
* Tables aren't strictly *required* to have a primary key...
   * ...However, defining a primary key is a) best practice; b) nearly always helpful for avoiding application bugs; and c) choosing a primary key will give you greater accuracy and thoughtfulness when modelling your problem space
   * We'll go over this more in through examples in the [Uniqueness] section below.

**Foreign keys**

* Here are some of the main things that foreign keys do:
   * Make relationships across different tables more explicit, which supports readability and maintainability
   * Enforce dependencies between tables, which supports validation and correctness
   * May speed up join operations
   * May slow down insert operations
* A table can have any number of foreign keys, and it will only sometimes make sense to add to a table.
   * Generally, if you expect one of your tables to have a dependency on another table -- where the value in a column on table A should only exist if the value already exists in a column on table B -- then you'll probably want to define a foreign key.

### Constraints

**Indexes**

* Indexes are ALL about performance -- defining good indexes on your tables is critical to optimizing your operations, and not using them is going to cause you to miss out on some huge performance boosts.
* However, adding indexes left and right is NOT the takeaway here. Indexes typically speed up some operations and slow down other operations. Additionally, indexes also have a storage cost.
* TODO: talk about types of scans, maybe some under-the-hood stuff
   * [TODO: put this somewhere] Think: retrieving an item by scanning through a whole list to find it (linear time complexity) vs. retrieving an item by directly accessing it in a key-value store (constant time complexity).

**Uniqueness**

**Other Constraints**

* Default values
* NULL-ness
* Value validation

## what is it for

## what is it good at

## what is it bad at

## Best Practices

### Authentication

### Transactions + locking

### Schema design

### Performance

When considering performance as well, it's crucial to have a good understanding of how your application uses/will use your database. Will you be inserting lots of data to this table, but rarely reading it? Will you be reading the data from this table a lot, but inserting or deleting the table's data less often? And it's not just about the sheer volume of operations - maybe you need to insert data relatively more often than read it; but when you do perform reads, they need to be lightning fast, whereas the latency of your many many inserts matters less. Another question to consider is, are your data access patterns predictable and consistent for this table, or will they vary a lot?

How do we answer these questions? Some practical hot tips:

* Observe your application's behaviour (observability is probably an entire topic to include)
* Learn how to read execution plans


### Read replicas

## related topics

**Servers + Clients**
**Local vs Remote**
