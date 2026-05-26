import datetime

message = input("Enter a message to log: ")


now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

log_entry = f"[{timestamp}] {message}\n"

with open("log.txt", "a") as file:
    file.write(log_entry)

print("Log written successfully to log.txt!")