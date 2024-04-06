package db

import (
	"database/sql"
	"errors"
	"fmt"

	// need this to make it clear to the database/sql package what kind
	// of database (specifically: database driver) we're using
	//
	// the `_` just means that while we DO want this to be imported, we're not
	// actually (directly) using anything from the package in this file
	_ "github.com/go-sql-driver/mysql"

	"github.com/jmoiron/sqlx"
)

// TODO: actually do something here
type DB struct {
	db     *sqlx.DB
	config *Config
}

type Config struct {
	User         string
	Password     string
	Host         string
	Port         string
	DatabaseName string
}

func (c *Config) Validate() error {
	// TODO: make sure all values are accounted for and present
	return nil
}

func (c *Config) ConnectionStr() string {
	return fmt.Sprintf("mysql://%s:%s@tcp(%s:%s)/%s", c.User, c.Password, c.Host, c.Port, c.DatabaseName)
}

func NewDB(config *Config) (*DB, error) {
	if config == nil {
		return nil, errors.New("no config provided")
	}
	if err := config.Validate(); err != nil {
		return nil, err
	}

	db, err := sql.Open("mysql", config.ConnectionStr())
	if err != nil {
		return nil, err
	}
	dbx := sqlx.NewDb(db, "mysql")

	return &DB{
		db:     dbx,
		config: config,
	}, nil
}
