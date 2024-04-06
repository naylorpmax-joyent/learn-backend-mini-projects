package api

import (
	"encoding/json"
	"log"
	"net/http"

	"github.com/google/uuid"
	"github.com/naylorpmax-joyent/reminders/pkg/reminder"
)

type Handler struct {
	Service *reminder.Service
}

func (h *Handler) Create(w http.ResponseWriter, r *http.Request) {
	log.Println("creating a new reminder!")

	w.WriteHeader(http.StatusAccepted)
	json.NewEncoder(w).Encode(&CreateReminderResponse{
		ReminderID: uuid.New().String(),
	})
}

func (h *Handler) List(w http.ResponseWriter, r *http.Request) {
	log.Println("listing reminders!")
	w.WriteHeader(http.StatusOK)
	w.Header().Set("Content-Type", "application/json; charset=utf-8")

	json.NewEncoder(w).Encode(&ListRemindersResponse{
		Reminders: []Reminder{
			{
				Name:      "take your meds",
				ID:        "088b39e4-0ab1-4923-b352-481acaeaa2ed",
				Frequency: "daily",
				Time:      "9am",
			},
			{
				Name:      "feed the cats! 🐈",
				ID:        "259da3e6-01ee-4361-a26a-b19f52aa71cf",
				Frequency: "daily",
				Time:      "7pm",
			},
		},
	})
}

func (h *Handler) Get(w http.ResponseWriter, r *http.Request) {
	log.Println("getting a specific reminder!")
	w.WriteHeader(http.StatusOK)
}

func (h *Handler) Delete(w http.ResponseWriter, r *http.Request) {
	log.Println("deleting a specific reminder!")
	w.WriteHeader(http.StatusAccepted)
}
