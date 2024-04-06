package api

type CreateReminderRequest struct {
	Name string `json:"name"`
	Time string `json:"time"`
	Day  string `json:"day"`
}

type CreateReminderResponse struct {
	ReminderID string `json:"reminderId"`
}

type GetReminderRequest struct {
	ReminderID string `json:"reminderId"`
}

type GetReminderResponse struct {
	// this is an anonymous nested struct
	Reminder
}

type DeleteReminderRequest struct {
	ReminderID string `json:"reminderId"`
}

type ListRemindersRequest struct {
	Limit int `json:"limit"`
}

type ListRemindersResponse struct {
	Reminders []Reminder `json:"reminders"`
}
