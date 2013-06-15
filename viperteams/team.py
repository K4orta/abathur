class Team:
	def __init__(self):
		self.__id = None
		self.__name = "TBD"
		self.country = None
		self.race = "random"
		self.full_name = None
		self.full_name_ko = None
		self.slug = None
		self.image_url = None

	@property 
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		self.__name = name

	@property 
	def id(self):
		return self.__id

	@id.setter
	def id(self, id):
		self.__id = id