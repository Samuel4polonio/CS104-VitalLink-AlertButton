import time
import RPi.GPIO as GPIO
import requests

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

BOT_TOKEN = "8824843415:AAHSpWQEU8K8sg9riOZ7tO8wQ_dvup_r-U8"
CHAT_ID = "8957652411"



button_pressed = False


while True:
    if GPIO.input(7) == GPIO.HIGH and not button_pressed:
        print("Someone pressed the alert button!")

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        data = {
            "chat_id": CHAT_ID,
            "text": "Someone pressed the alert button!"
        }

        response = requests.post(url, json=data)


    elif GPIO.input(7) == GPIO.LOW:
        button_pressed = False

    time.sleep(0.1)
