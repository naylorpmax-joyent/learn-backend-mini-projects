package api

import (
	"net/http"

	"github.com/gorilla/mux"
)

func Router(reminders *Handler) *mux.Router {
	router := mux.NewRouter()

	// create a new reminder
	router.Path("/reminders").
		Methods(http.MethodPost).Name("CreateReminder").HandlerFunc(reminders.Create)

	// list many reminders
	router.Path("/reminders").
		Methods(http.MethodGet).Name("ListReminders").HandlerFunc(reminders.List)

	// get a specific reminder
	router.Path("/reminders/reminder_id:{[a-zA-Z0-9-]+}").
		Methods(http.MethodGet).Name("GetReminder").HandlerFunc(reminders.Get)

	// delete a specific reminder
	router.Path("/reminders/reminder_id:{[a-zA-Z0-9-]+}").
		Methods(http.MethodDelete).Name("DeleteReminder").HandlerFunc(reminders.Delete)

	// catch-all
	router.PathPrefix("/").HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusNotFound)
	})

	return router
}
