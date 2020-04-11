#!/bin/bash
# Delete Request
curl -s -o /dev/null -I -w "%{http_code}" "$1"
