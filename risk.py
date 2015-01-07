# pt = per tern
#5
north_america = [ 'alaska',
			'alberta',
			'northwest territory',
			'ontario',
			'western united states',
			'eastern united states',
			'central america',
			'eastern canada',
			'greenland' ];
# 2
south_america = [ 'venezuela',
			'peru',
			'argentina',
			'brazil' ];
# 2
australia = [ 'western australia',
			'eastern australia',
			'new guinea',
			'indonesia' ];
# 3
africa = [ 'north africa',
			'egypt',
			'central africa',
			'east africa',
			'south africa',
			'madagascar' ];
# 4
europe = [ 'iceland',
			'great britain',
			'western europe',
			'eastern europe',
			'northern europe',
			'southern europe',
			'scandanavia',
			'russia' ];
# 7
asia = [ 'kamchatka',
			'china',
			'afghanistan',
			'india',
			'irkutsk',
			'japan',
			'middle east',
			'mongolia',
			'siam',
			'siberia',
			'ural',
			'yakutsk' ];
class countries:
	def neighbouring(self, c):
		c=c.lower()
		# North America (5 pt)
		if c==north_america[0]:
			nb = { 1 : 'Alberta',
			2 : 'Northwest Territory' }

		elif c==north_america[1]:
			nb = { 1 : 'Alaska',
			2 : 'Greenland',
			3 : 'Ontario',
			4 : 'Northwest Territory',
			5 : 'Western United States' }

		elif c==north_america[2]:
			nb = { 1 : 'Alaska',
			2 : 'Alberta',
			3 : 'Greenland',
			4 : 'Ontario' }

		elif c==north_america[3]:
			nb = { 1 : 'Alberta', 
			2 : 'Eastern Canada',
			3 : 'Eastern United States',
			4 : 'Greenland', 
			5 : 'Northwest Territory',
			6 : 'Western United States' }
		
		elif c==north_america[4]:
			nb = { 1 : 'Alberta',
			2 : 'Central America',
			3 : 'Eastern United States',
			4 : 'Ontario' }
		elif c==north_america[5]:
			nb = { 1 : 'Central Amerca',
			2 : 'Eastern Canada',
			3 : 'Ontario',
			4 : 'Western United States' }
		elif c==north_america[6]:
			nb = { 1 : 'Eastern United States',
			2 : 'Venezuela', # South America
			3 : 'Western United States' }
		elif c==north_america[7]:
			nb = { 1 : 'Eastern United States',
			2 : 'Greenland',
			3 : 'Ontario' }
		elif c==north_america[8]:
			nb = { 1 : 'Eastern Canada',
			2 : 'Iceland', # Europe
			3 : 'Northwest Territory',
			4 : 'Ontario' }
		# South America (2pt)
		elif c==south_america[0]:
			nb = { 1 : 'Central America',
			2 : 'Brazil',
			3 : 'Peru',
			4 : 'Central America' }
		elif c==south_america[1]:
			nb = { 1 : 'brazil',
			2 : 'argentina',
			3 : 'venezuela' }
		elif c==south_america[2]:
			nb = { 1 : 'peru',
			2 : 'brazil' }
		elif c==south_america[3]:
			nb = { 1 : 'venezuela',
			2 : 'peru',
			3 : 'argentina',
			4 : 'north africa' } # Africa
		# Australia (2pt)
		elif c==australia[0]:
			nb = { 1 : 'eastern australia',
			2 : 'new guinea',
			3 : 'indonesia' }
		elif c==australia[1]:
			nb = { 1 : 'western australia',
			2 : 'new guinea', }
		elif c==australia[2]:
			nb = { 1 : 'indonesia',
			2 : 'western australia',
			3 : 'eastern australia' }
		elif c==australia[3]:
			nb = { 1 : 'siam', # Asia
			2 : 'new guinea',
			3 : 'western australia' }

		return nb
	def continent(self, c):
		c=c.lower()
		if c in asia:
			return "asia"
		elif c in europe:
			return "europe"
		elif c in africa:
			return "africa"
		elif c in north_america:
			return "north america"
		elif c in south_america:
			return "south america"
		elif c in australia:
			return "australia"
	def print_all(self):
		for x in range(0, len(asia)):
			print(asia[x].title())
		for x in range(0, len(europe)):
			print(asia[x].title())
		for x in range(0, len(africa)):
			print(asia[x].title())
		for x in range(0, len(north_america)):
			print(asia[x].title())
		for x in range(0, len(south_america)):
			print(asia[x].title())
		for x in range(0, len(australia)):
			print(asia[x].title())
foo = countries()
print('Countries are: ')
nb = foo.neighbouring("ONTARIO")
for x in range(1, len(nb)+1):
	print(nb[x].title())
print("")
print("")


