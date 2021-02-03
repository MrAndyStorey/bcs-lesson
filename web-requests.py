#!/usr/bin/env python3

import requests as req

# Regex Pattern will return full match including the html tags and group 1 () as the contents
regex_pattern = r"\<title\>(.+?)\<\/title\>"

# URL to check
url = "https://httpd.apache.org/"
