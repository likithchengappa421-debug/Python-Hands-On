import requests
import datetime

# 1. THE BACKEND: Call the API
print("Connecting to the International Space Station API...")
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()  # This converts the internet JSON into a Python Dictionary

# 2. THE DATA ENGINEERING: Extract only the names
number_in_space = data["number"]
astronauts = data["people"]

print(f"\nThere are currently {number_in_space} humans in space right now.")

# 3. THE DEVOPS: Log it to a file
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("space_log.txt", "a") as file:
    file.write(f"[{timestamp}] Active Astronauts: ")

    for person in astronauts:
        name = person["name"]
        print(f"- {name}")  # Print to your screen
        file.write(f"{name}, ")  # Save to your hard drive

    file.write("\n")

print("\nData successfully logged to space_log.txt")