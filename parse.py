#! /usr/bin/python
import urllib.request
import urllib.parse
import json
from pprint import pprint

# Local Files
# EDIT THIS TO MATCH YOUR ASTRAL FILE
json_file='astral_data.json' 
# EDIT THIS WITH YOUR Oauth KEY 
Oauth = ""

# Read File 
json_data=open(json_file)
data = json.load(json_data)
json_data.close()

file = open('OUTPUT', 'w')
found = True
# Request 
url = 'https://api.github.com/repositories/'
for x in data:
    for y in data[x]["tags"]:
        if (y["name"] == "unixporn"):
            found = True
    
    if found:
        try:
            f = urllib.request.urlopen(url+str(data[x]["repo_id"])+"?access_token="+str(Oauth))
            
            JSON_object = json.loads(f.read().decode('utf-8', errors='replace'))
            out = str(JSON_object["name"])+ " - " + str(JSON_object["full_name"])+" : "+ str(JSON_object["description"])+ "     (" + str(JSON_object["html_url"] + ")\n")
            print(out)
            file.write(out)
        except:
            pass
    
    found = False
        
file.close()