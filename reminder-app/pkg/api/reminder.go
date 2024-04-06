package api

type Reminder struct {
	// TODO: this is gonna need some WORK at some point...
	Name      string `json:"name"`
	ID        string `json:"id"`
	Time      string `json:"time"`
	Frequency string `json:"frequency"`
}
