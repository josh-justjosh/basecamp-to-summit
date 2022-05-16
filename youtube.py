import requests
from time import sleep

while True:
    climbs = requests.get("https://sequematic.com/variable-get/2293/85A7210D14/Climbing/").text
    print(climbs)
    with open('climbs.txt',mode='w') as f:
        f.write(climbs)
    sleep(15)
