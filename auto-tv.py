import xmltodict, datetime
import requests

url = "http://192.168.1.72:32400/library/sections/1/all"
#url = "http://localhost:32400/library/sections/1/all"

r = requests.get(url)

if(r.status_code == 200):
	data = xmltodict.parse(r.text)
	movie = data['MediaContainer']['Video']
	for mv in movie:
		print "-----------------------------------"
		print mv['@title']
		if "@duration" in mv:
			print " -> " + str(datetime.timedelta(seconds=int(mv['@duration'])/1000))
		if '@rating' in mv:
			print " -> " + (mv['@rating'])[:4] + "/10"
		if '@year' in mv:
			print " -> " + mv['@year']
		if 'Genre' in mv:
			print " -> Genre: "
			for genreTags in mv['Genre']:
				if isinstance(genreTags, dict):
					for key, genre in genreTags.iteritems():
						if key == "@tag":
							print " ---> " + genre
				elif isinstance(mv['Genre'], dict):
					print " ---> " + mv['Genre']['@tag']
		if 'Part' in mv['Media']:
			if isinstance(mv['Media']['Part'], dict):
				for key, string in mv['Media']['Part'].iteritems():
					if key == "@key":
						print string
			else:
				for partItem in mv['Media']['Part']:
					for key, string in partItem.iteritems():
						if key == "@key":
							print string
						



