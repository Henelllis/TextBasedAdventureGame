class character(object):


	def __init__(self , name):
		self.__name = name
		self.__hp = 5
		self.__attack = 2
		self.__defence = 2
		self.__atacks = 1
		self.__exp	  = 0

	def get_name(self):
		return self.__name

	def set_name(self, name):
	#	if health
		self.__name = name

	def get_hp(self):
		return self.__hp

	def set_hp(self, hp):
	#	if health
		self.__hp = hp

	def get_attack(self):
		return self.__attack

	def set_attack(self, attack):
	#	if health
		self.__hp = hp

	def get_defence(self):
		return self.__defence

	def set_defence(self, defence):
	#	if health
		self.__defence = defence

	def get_exp(self):
		return self.__exp

	def set_exp(self, exp):
	#	if health
		self.__hp = hp