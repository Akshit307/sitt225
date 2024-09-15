import serial
import time
import pyrebase

# Firebase configuration
config = {
  "apiKey": "AIzaSyCBS8-udBvFVvLd1BdLaLcWxnkT7kCjNkI",
  "authDomain": "clouddata-8b78d.firebaseapp.com",
  "databaseURL": "https://clouddata-8b78d-default-rtdb.firebaseio.com",
  "storageBucket": "clouddata-8b78d.appspot.com",
  "messagingSenderId": "915663157900",
  "appId": "1:915663157900:web:c692bf4474fa286ae119a9",
  "measurementId": "G-685NSL0Y91"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Set up serial communication with Arduino
ser = serial.Serial('COM7', 9600) 
while True:
    if ser.in_waiting > 0:
        # Read data from Arduino
        data = ser.readline().decode('utf-8').strip()

        # Remove labels (like "X: ", "Y: ", "Z: ") and split the data
        data = data.replace("X: ", "").replace("Y: ", "").replace("Z: ", "")
        x, y, z = data.split(',')

        # Create a data dictionary with timestamp
        data_to_upload = {
            'timestamp': time.time(),
            'x': float(x),
            'y': float(y),
            'z': float(z)
        }

        # Upload data to Firebase
        db.child("gyroscope_data").push(data_to_upload)

        print("Data uploaded: ", data_to_upload)

        time.sleep(0.05)  # Delay to avoid overwhelming Firebase
