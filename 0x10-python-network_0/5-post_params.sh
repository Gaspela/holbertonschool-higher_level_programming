#!/bin/bash
# Sends a POST request with data
# -s, --silent
# -d, --data <email>
# &subject text
# "$1" Number parmeters received
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
