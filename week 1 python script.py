import serial
import time
import random

# Connect to the Arduino
arduino = serial.Serial('COM7', 9600) 

while True:
    # Send a random number to the Arduino
    random_number = random.randint(1, 5)
    print(f"Sending {random_number} to Arduino at {time.ctime()}")
    arduino.write(f"{random_number}\n".encode())

    # Wait for the Arduino to blink and send a random number back
    time.sleep(1)
    if arduino.in_waiting > 0:
        data = arduino.readline().decode().strip()
        print(f"Received {data} from Arduino at {time.ctime()}")
        
        # Wait for the number of seconds sent by Arduino
        time_to_sleep = int(data)
        print(f"Sleeping for {time_to_sleep} seconds...")
        time.sleep(time_to_sleep)
