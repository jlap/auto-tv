import datetime

class Media:
	duration = 0
	def __init__(self, media):
		self.title = media['@title']
		
		self.duration = media['@duration']
		
		#Parse parts to get the file path
		#TODO: Handle whenever a movie comes in several parts
		if 'Part' in media['Media']:
			if isinstance(media['Media']['Part'], dict):
				for key, string in media['Media']['Part'].iteritems():
					if key == "@key":
						self.key =  string
			else:
				for partItem in media['Media']['Part']:
					for key, string in partItem.iteritems():
						if key == "@key":
							self.key =  string

		self.genres = []
		# Get the genres
		if 'Genre' in media:
			for genreTags in media['Genre']:
				if isinstance(genreTags, dict):
					for key, genre in genreTags.iteritems():
						if key == "@tag":
							self.genres.append(genre)
				elif isinstance(media['Genre'], dict):
					self.genres.append(media['Genre']['@tag'])
		return self
