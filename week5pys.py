import pyrebase
import pandas as pd

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

# Fetch all data from Firebase
data = db.child("gyroscope_data").get().val()

# Convert the data into a Pandas DataFrame
df = pd.DataFrame(data).T  # .T to transpose since Firebase stores data as nested dictionaries
df.columns = ['timestamp', 'x', 'y', 'z']

# Save to CSV
df.to_csv('gyroscope_data.csv', index=False)

print("Data saved to CSV!")
