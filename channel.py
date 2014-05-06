import random 

class Channel:
	def __init__(self, name):
		self.name = name
		self.movies = []
		self.schedule = []

	def addMovie(self, movie):
		self.movies.append(movie)
	
	#For now we just shuffle the movie list.
	#when we get to support TV shows, that'll have to be redone to try to
	# play the episodes in at least a somewhat orderly fashion
	def buildSchedule(self, time):
		timeSoFar = 0
		i = 0
		random.shuffle(self.movies)
		while timeSoFar < time:
			if i == len(self.movies):
				i = 0
			else: 
				i+=1
			self.schedule.append(self.movies[i])	
			timeSoFar += int(self.movies[i].duration)
