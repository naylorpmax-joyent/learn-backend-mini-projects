package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"time"

	"github.com/naylorpmax-joyent/reminders/pkg/api"
	"github.com/naylorpmax-joyent/reminders/pkg/db"
	"github.com/naylorpmax-joyent/reminders/pkg/reminder"
)

func main() {
	// TODO: we should probably use a real logger (zap) eventually
	// TODO: gonna need a fewwww more environment variables before this is done

	db, err := db.NewDB(&db.Config{
		User:         getEnvOrElse("DB_USER"),
		Password:     getEnvOrElse("DB_PASSWORD"),
		Host:         getEnvOrElse("DB_HOST"),
		Port:         getEnvOrElse("DB_PORT"),
		DatabaseName: getEnvOrElse("DB_NAME"),
	})
	if err != nil {
		panic(err)
	}

	s := &reminder.Service{DB: db}
	handler := &api.Handler{Service: s}
	router := api.Router(handler)

	server := &http.Server{
		Handler:      router,
		Addr:         ":8000",
		WriteTimeout: 5 * time.Second,
		ReadTimeout:  5 * time.Second,
	}

	log.Println("listening on :8000")
	log.Fatal(server.ListenAndServe())
}

func getEnvOrElse(k string) string {
	v := os.Getenv(k)
	if v == "" {
		panic(fmt.Errorf("missing environment variable (must not be empty): %s", k))
	}
	return v
}
