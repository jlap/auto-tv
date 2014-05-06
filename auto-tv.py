import xmltodict, datetime
import requests
from movie import Movie
from genre import Genre
from channel import Channel
from tv import TV
from collections import Counter
import simplejson
import time

url = "http://192.168.1.72:32400"
#url = "http://localhost:32400"
r = requests.get(url+"/library/sections/1/all")

if(r.status_code == 200):
	#Request a list with all movies
	data = xmltodict.parse(r.text)
	moviesData = data['MediaContainer']['Video']
	movies = [];
	for mv in moviesData:
		# request metadata for each individual movie
		movieMetadataRequest = requests.get(url+mv['@key'])
		if movieMetadataRequest.status_code == 200:
			data = xmltodict.parse(movieMetadataRequest.text)
			movie = data['MediaContainer']['Video']
			try:
				newMovie = Movie(movie)
				movies.append(newMovie)
			except:
				continue
				#we do nothing, that means the movie is malformed

	genres = []
	# Reverse everything; we want to know how many movies each genre has
	for mv in movies:
		for genre in mv.genres:
			found = False
			for g in genres:
				if genre == g.name:
					g.addMovie(mv)
					found = True
			if not found:
				newGenre = Genre(genre)
				newGenre.addMovie(mv)
				genres.append(newGenre)
	
	# Sort them by number of movies
	genres = sorted(genres, key=lambda x: x.movieCount, reverse=True)
		
	# We build some channels from the 10 heaviest genres
	channels = []
	i=0
	for genre in genres:
		newChannel = Channel(genre.name)
		for mv in genre.movies:
			newChannel.addMovie(mv)
		newChannel.buildSchedule(86400000)
		channels.append(newChannel)
		del genre

		i+=1
		if i > 10:
			break

	#Serialize the channels and write them to a json	
	data = []
	for channel in channels:
		moviesData = []
		for mv in channel.schedule:
			moviesData.append(dict({
				"title":mv.title,
				"key":mv.key,
				"duration":mv.duration
			}))

		data.append(dict({'channel':dict({
				"channelName":channel.name,
				"channelStarted":int(round(time.time() * 1000)),
				"movies":moviesData
			})}))

	with open('channels.json', 'w') as f:
		simplejson.dump(data, f)
	
	
