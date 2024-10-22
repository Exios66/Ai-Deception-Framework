#!/bin/bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --port=8000 --cert=adhoc
