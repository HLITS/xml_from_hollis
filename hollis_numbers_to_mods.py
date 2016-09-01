import requests
import csv
import codecs
import time

in_file = 'ECDAScannedToSend.csv' # to do: create prompt
out_file = 'ECDAScannedToSend.xml' # to do: create prompt

with open(in_file, 'Ur') as f:
    data = list(tuple(rec) for rec in csv.reader(f, delimiter=',')) 

hollis_number = data[0].index('Hollis Number') # assumes that first line ([0]) is headers, not data, and that Hollis numbers are in a column labeled "Hollis Number"

xml_urls = []

for datum in data[1:]: # assumes that data starts with the second line ([1:])
    xml_urls += [datum[hollis_number]]

format = "mods" # to do: create prompt
xml_content = ""

for url in xml_urls:
    xml_content += requests.get("http://webservices.lib.harvard.edu/rest/" + format + "/hollis/" + url).text 
    time.sleep(1)

xml_file = open(out_file, "wb")
xml_file.write(xml_content.encode('utf-8')) # to do: strip off superfluous xml & mods tags, or write separate files
xml_file.close()
