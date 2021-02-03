#!/usr/bin/env python3

import requests as req

# Regex Pattern will return full match including the html tags and group 1 () as the contents
regex_pattern = r"\<title\>(.+?)\<\/title\>"

# URL to check - ideally the school URL to ensure a suitable response
exampleURL = "https://httpd.apache.org/"

#Example 1
def serverstatus(url):
  resp = req.get(url)
  if resp.status_code ==200:
      return "{} OK".format(url)
  else:
      return "{} returned an error {}".format(url, resp.status_code)

# 200 is a standard response for successful HTTP requests
# 404 tells that the requested resource could not be found.
# More details here: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

print(serverstatus(exampleURL))
print(serverstatus(exampleURL + "xxxxxxxxx"))


def titleofpage(url):
  resp = req.get(url)
  if resp.status_code ==200:
    #Get the page content and search for the <title> start and ending tags
    start = resp.text.find('<title>') + 7
    end = resp.text.find('</title>', start)
    if start > 0:
        return "{}".format(resp.text[start:end])
    else:
        return "<title> tag not found."
  else:
      return "{} returned an error {}".format(url, resp.status_code)

print(titleofpage(exampleURL))

