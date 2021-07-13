import tweepy
#from watchdog.observers import Observer
import os
import time
import RPi.GPIO as GPIO

# Authenticate to Twitter
auth = tweepy.OAuthHandler("02zd69hYsOIkB8OOTZO1RMfug", "lnvVAnzizpe8KjT1BZOILnl8lAinNT00UwXidlh4OgmED1c1l6")
auth.set_access_token("1406192250481164291-nbDcuQcX1gq5Nl313ahUz0kFIUSlaE", "7UlzWmd93qymGFr66pg6M1RWlC9AVR6BCyzquedN5cHAT")

# Create API object
api = tweepy.API(auth)
GPIO.setmode(GPIO.BOARD)
sensor = GPIO.setup(3, GPIO.IN)

while True:
	
	if (GPIO.input(3)):
		print("Funciono!")
	
	status="Prova fotos"
#Find new pic 
	arr = os.listdir('Fotos/')
	if len(arr)!=0:
		foto=arr[0];
		
		time.sleep(1)

		directory="Fotos/" + foto
		#Post the theet
		api.update_with_media(directory, status)
		#Remove the pic
		os.remove(directory)
		pass
	time.sleep(1)
