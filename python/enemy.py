import os
import sys


class enemy(object):


	def __init__(self , hp , attack, defence, attacks, name ):
		self.__hp = hp
		self.__attack = attack
		self.__defence = defence
		self.__name = name
		self.__atacks = attacks
		self.__curhealth = hp

	def get_hp(self):
		return self.__hp

	def set_hp(self, hp):
	#	if health
		self.__hp = hp

	def get_attack(self):
		return self.__attack

	def set_attack(self, attack):
	#	if health
		self.__attack = attack

	def get_defence(self):
		return self.__defence

	def set_defence(self, defence):
	#	if health
		self.__defence = defence

	def get_name(self):
		return self.__name

	def set_attack(self, name):
	#	if health
		self.__name = name

	def get_curhealth(self):
		return self.__curhealth

	def set_curhealth(self, curhealth):
	#	if health
		self.__curhealth = curhealth


##Honestly just a test for inheritance
class taxedermist(enemy):
	"""docstring for ClassName"""
	def __init__(self, hp , attack , defence , attacks,name):
		super(self.__class__, self).__init__(hp , attack , defence , attacks,name)
		
		

