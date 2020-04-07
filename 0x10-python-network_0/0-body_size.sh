#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept.
# -s, --silent
# -I, --head
# "$1" Number parmeters received
# -i, --include
# cut -d "delimitador"
# -f (field)
curl -sI "$1" | grep -i Content-Length | cut -d ' ' -f2-
