import datetime

def logMessage(text):
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-2]+ "Z"
    print(f"{timestamp} {text}")
