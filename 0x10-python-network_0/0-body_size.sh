#!/bin/bash
#takes and sends a request to URL and displays the size of the body of response
curl -s "$1" | wc -c
