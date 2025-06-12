import time
import board
import adafruit_dht

# Use DHT11 or DHT22
# dht_device = adafruit_dht.DHT11(board.D4)  # For DHT11
dht_device = adafruit_dht.DHT22(board.D4)    # For DHT22
# Change `board.D4` to your actual GPIO pin

print("Reading DHT sensor...")

try:
    while True:
        try:
            temperature_c = dht_device.temperature
            humidity = dht_device.humidity

            if temperature_c is not None and humidity is not None:
                print(f"Temp: {temperature_c:.1f} °C  |  Humidity: {humidity:.1f} %")
            else:
                print("Sensor returned no data.")

        except RuntimeError as e:
            print(f"Runtime error: {e}")
            # Don't crash program; wait and retry
            time.sleep(2)
            continue

        time.sleep(2)

except KeyboardInterrupt:
    print("Program stopped by user.")

finally:
    dht_device.exit()
