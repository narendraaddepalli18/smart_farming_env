import requests

url = "https://your-space-url"  # replace this

print("Reset:", requests.get(f"{url}/reset").json())

actions = ["irrigate", "fertilize", "irrigate", "fertilize", "harvest"]

for action in actions:
    res = requests.get(f"{url}/step/{action}")
    print(res.json())