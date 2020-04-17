#!/usr/bin/python3
# Takes in URL and email, sends a POST request,
# And displays the body of the response.
import requests
from sys import argv


if __name__ == "__main__":
    email = {'email': argv[2]}
    r = requests.post(argv[1], data=email)
    print(r.text)
