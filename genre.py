class Genre:
	def __init__(self, name):
		self.name = name
		self.movies = []
		self.movieCount = 0

	def addMovie(self, movie):
		self.movies.append(movie)
		self.movieCount += 1

	def getNumberOfMovies(self):
		return self.movieCount
