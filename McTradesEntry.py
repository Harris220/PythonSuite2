class McTradesEntry:
	def __init__(self,name,title,date,rating):
		self.name = name
		self.title = title
		self.date = date
		self.rating = rating
		
	def setName(self,newName):
		self.name = newName
	def getName(self):
		print(self.name)
	def setTitle(self,newTitle):
		self.title = newTitle
	def getTitle(self):
		print(self.Title)
	def setDate(self,newDate):
		self.date = newDate
	def getDate(self):
		print(self.date)
	def setRating(self,newRating):
		self.rating = newRating
	def getRating(self):
		print(self.rating)
		