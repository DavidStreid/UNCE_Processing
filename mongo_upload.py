import json
import requests

url = "..."

file = 'unce_file.json'
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
