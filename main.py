import urllib.request
import json
import datetime
import random
import string
import time
# import os
# import sys

ids = [
  "7371c6df-41a8-40f2-8e09-5690db0e136e",
  "44e43bad-40b7-4932-8107-273fd1bdcd7d",
  "69dd16ae-394b-476e-8f5f-fc11dc3c8235"
]

ids_count = ids.__len__()

#os.system("title WARP-PLUS-CLOUDFLARE By ALIILAPRO")
#os.system('cls' if os.name == 'nt' else 'clear')
print('     ___   _____   _____  __    __  _   _   _____   _____   _____  \n'
      '    /   | |  _  \ |_   _| \ \  / / | | | | /  _  \ /  ___| /  _  \ \n'
      '   / /| | | |_| |   | |    \ \/ /  | |_| | | |_| | | |___  | |_| | \n'
      '  / / | | |  ___/   | |     |  |   \___  | |  _  | |  _  \ \___  | \n'
      ' / /  | | | |       | |    / /\ \      | | | |_| | | |_| |  ___| | \n'
      '/_/   |_| |_|       |_|   /_/  \_\     |_| \_____/ \_____/ |_____/ \n')
print("[+] ABOUT SCRIPT:")
print("[-] With this script, you can getting unlimited GB on Warp+.")
print("[-] Version: 4.0.0")
print("--------")
print("[+] THIS SCRIPT CODDED BY TONY-APTX4869")
print("[-] SITE: github.com/tony-aptx4869")
print("[-] TELEGRAM: tonychang1069")
print("--------")


def genString(stringLength):
  try:
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))
  except Exception as error:
    print(error)


def digitString(stringLength):
  try:
    digit = string.digits
    return ''.join((random.choice(digit) for i in range(stringLength)))
  except Exception as error:
    print(error)


url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'


def run(referrer):
  try:
    install_id = genString(22)
    body = {"key": "{}=".format(genString(43)),
            "install_id": install_id,
            "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
            "referrer": referrer,
            "warp_enabled": False,
            "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
            "type": "Android",
            "locale": "es_ES"}
    data = json.dumps(body).encode('utf8')
    headers = {'Content-Type': 'application/json; charset=UTF-8',
               'Host': 'api.cloudflareclient.com',
               'Connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip',
               'User-Agent': 'okhttp/3.12.1'
               }
    req = urllib.request.Request(url, data, headers)
    response = urllib.request.urlopen(req)
    status_code = response.getcode()
    return status_code
  except Exception as error:
    print(error)


g = 0
b = 0
while True:
  # os.system('cls' if os.name == 'nt' else 'clear')
  print("")
  print("            WARP-PLUS Script" + " By TONY-APTX4869")
  print("")
  id_n = 0
  for referrer in ids:
    result = run(referrer)
    id_n = id_n + 1
    if result == 200:
      g = g + 1
      # animation = ["[■□□□□□□□□□] 10%", "[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%",
      #              "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%",
      #              "[■■■■■■■■■■] 100%"]
      # for i in range(len(animation)):
      #   time.sleep(0.3)
      #   sys.stdout.write(f"\r[{id_n}/{ids_count}] Preparing... " + animation[i % len(animation)])
      #   sys.stdout.flush()
      sec = random.uniform(1, 3)
      time.sleep(sec)
      print(f"[{id_n}/{ids_count}] This ID is processing... ")
      print(f"[-] WORK ON ID: {referrer}")
      print(f"[:)] {g} GB has been successfully added to your account.")
      print(f"[#] Total: {g} Good {b} Bad")
      if id_n != ids_count:
        sec = random.uniform(60, 120)
        print(f"[*] After {sec} seconds, the next id will be be processed.")
        time.sleep(sec)
    else:
      b = b + 1
      print(f"[-] WORK ON ID: {referrer}")
      print("[:(] Error when connecting to server.")
      print(f"[#] Total: {g} Good {b} Bad")
  sec = random.randint(60, 180)
  print(f"[*] After {sec} seconds, {ids_count} new request(s) will be sent.")
  time.sleep(sec)
