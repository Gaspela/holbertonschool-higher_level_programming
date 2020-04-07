#!/bin/bash
# HTTP methods the server will accept.
# -s, --silent
# -I, --head
# "$1" Number parmeters received
# grep "Allow" (methods allowed)
# cut -d "delimitador"
# -f (field)
curl -sI "$1" | grep "Allow" | cut -d' ' -f2-
