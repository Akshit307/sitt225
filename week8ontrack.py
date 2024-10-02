import requests
import csv
from datetime import datetime


client_id = "siSgVZ7AhfbIU6Yds2C7rOKjnNPcy9wj"
client_secret = "J3olh9zOhHanRqkhl2ozj0J2g90bgMYnQCzGidmqA5mY0JNq4fcaOQ1ppqkVBIqB"
token_url = "https://api2.arduino.cc/iot/v1/clients/token"

device_id = "1c8c3ab4-e29e-435f-a2f0-baeacd61a185"
property_id_x = "d5712fb8-1499-4459-8af7-e6f1d32b89d8"
property_id_y = "82c65e12-1589-4af0-9e5b-707ca00b4be8"
property_id_z = "a579ea81-37a9-4182-bf5d-df55aff4af97"

def get_oauth_token():
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "audience": "https://api2.arduino.cc/iot"
    }

    response = requests.post(token_url, headers=headers, data=data)
    response_data = response.json()
    print(f"OAuth Token: {response_data['access_token']}")
    return response_data["access_token"]

# Fetch accelerometer data from Arduino Cloud
def fetch_accelerometer_data(token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Fetch X, Y, Z values
    url_x = f"https://api2.arduino.cc/iot/v2/things/{device_id}/properties/{property_id_x}"
    url_y = f"https://api2.arduino.cc/iot/v2/things/{device_id}/properties/{property_id_y}"
    url_z = f"https://api2.arduino.cc/iot/v2/things/{device_id}/properties/{property_id_z}"

    x_value = requests.get(url_x, headers=headers).json().get("last_value")
    y_value = requests.get(url_y, headers=headers).json().get("last_value")
    z_value = requests.get(url_z, headers=headers).json().get("last_value")

    print(f"Fetched X: {x_value}, Y: {y_value}, Z: {z_value}")
    return x_value, y_value, z_value

# Write data to CSV file
def write_data_to_csv(x, y, z):
    with open("accelerometer_data.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), x, y, z])

# Main code to run the data-fetching loop
if __name__ == "__main__":
    token = get_oauth_token()

    # Write CSV headers
    with open("accelerometer_data.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "x", "y", "z"])

    while True:
        # Fetch the data
        x, y, z = fetch_accelerometer_data(token)
        if x is not None:
            write_data_to_csv(x, y, z)
