import json
import requests

url = "https://1460d9a8f89bd02f753745de07464cf0.balena-devices.com/postUNCE"
# "https://bf810d4f57af9fcd7329dada5c41b22c.balena-devices.com/postUNCE"
# "https://fe6dd65c26df38a8ae650cb6c9569f24.balena-devices.com//postUNCE"

file = '/Users/davidstreid/bioData/unce/unce_file.json'
with open(file) as f:
  data = json.load(f)
  entries = data["entries"]
  print("Sending updates for " + str(len(entries)) + " entries to " + url)
  # for entry in entries:
  for i in range(len(entries)):
    entry = entries[i]
    print("%d: %s" % (i, entry['unce_name']))
    r = requests.post(url, data = entry)
    if(r.status_code != 200):
        print("Failed: " + entry)

print("Done.")
