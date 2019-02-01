import tweepy
import requests
import os
import random


def twitter_api():
	CONSUMER_KEY = ''
	CONSUMER_SECRET = ''
	ACCESS_KEY = ''
	ACCESS_SECRET = ''

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api  = tweepy.API(auth)
	return api

def pick_random_file():
	return random.choice(os.listdir("./mylyrics/"))

def pick_random_image():
	return random.choice(os.listdir("./images/"))


def read_lyrics(inputtext):
	with open("./mylyrics/"+inputtext) as f:
		content = f.readlines()
		content = [x.strip() for x in content]
	n = 0
	createdlist = []
	for i in range(content.count('')+1):
		createdlist.append([])
	for i in content:
		if i !='':
			createdlist[n].append(i)
		else:
			n+=1
	#deleting all [] 
	myreadylist =  [x for x in createdlist if len(x) != 0]
	return myreadylist

def pick_random_lyric(lyric):
	# choice = random.choice(lyric)
	choice=''
	for i in random.choice(lyric):
		choice +=i+' '
	return choice

def final_touch():
	songname = pick_random_file()
	mylist = [pick_random_lyric(read_lyrics(songname)), songname[:-4]]
	return mylist

# words, filename = final_touch()

def tweet_image():
	artist =' #ArianaGrande' 
	api = twitter_api()
	words, filename = final_touch()
	print(words, filename)
	api.update_with_media("./images/"+pick_random_image(), words+filename+artist)


	#print(words, filename[:-4])
	

#newt = t[:-4]

# pick_random_lyric(read_lyrics(pick_random_file()))
# tweet_image()

#Post instagram pic + lyrics