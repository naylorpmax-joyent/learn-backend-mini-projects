#!/usr/bin/env bash

# TODO: mo better examples

curl -X POST \
	-H "content-type: application/json" \
	http://localhost:8000/reminders \
	-d '{
        "name": "take your meds",
        "time": "9am",
        "frequency": "daily"
    }' | jq

curl -X GET \
    -H "content-type: application/json; charset=utf-8" \
    http://localhost:8000/reminders | jq
