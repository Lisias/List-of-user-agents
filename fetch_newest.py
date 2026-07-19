import sys
import json
import urllib.request

def fetch_latest_browsers_data():
	URL = "https://www.browsers.fyi/api/"
	req = urllib.request.Request(URL)
	try:
		with urllib.request.urlopen(req, timeout=10) as response:
			raw_text = response.read().decode('utf-8')
			data = json.loads(raw_text)
		print(str(data))
	except requests.exceptions.JSONDecodeError as e:
		print("{:s}. Raw Output:".format(str(e)))
		print(response.text)
	except Exception as e:
		print("An unexpected error occurred: {:s}".format(str(e)))

def fetch_latest_browsers_useragents():
	URL = "https://jnrbsn.github.io/user-agents/user-agents.json"
	req = urllib.request.Request(URL)
	try:
		with urllib.request.urlopen(req, timeout=10) as response:
			raw_text = response.read().decode('utf-8')
			data = json.loads(raw_text)
		for ua in data:
			print(ua)
	except requests.exceptions.JSONDecodeError as e:
		print("{:s}. Raw Output:".format(str(e)))
		print(response.text)
	except Exception as e:
		print("An unexpected error occurred: {:s}".format(str(e)))

if __name__ == "__main__":
	for cmd in sys.argv[1:]:
		if 'data' == cmd: fetch_latest_browsers_data()
		if 'user-agent' == cmd: fetch_latest_browsers_useragents()
	
