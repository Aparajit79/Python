import json

default_settings = {
    "theme": "dark",
    "volume": 80,
    "notifications": True
}

def save_settings(settings):
    with open("settings.json", "w") as file:
    
        json.dump(settings, file, indent=4)
    print("Settings saved successfully!")


def load_settings():
    try:
        with open("settings.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
     
        print("No settings file found. Using defaults.")
        return default_settings




current_settings = load_settings()
print(f"Current Settings: {current_settings}")

try:
    new_volume = int(input("Enter new volume level (0-100): "))
    current_settings["volume"] = new_volume

    save_settings(current_settings)
    
except ValueError:
    print("Please enter a valid number.")