import os
import sys


class enemy(object):


	def __init__(self , hp , attack, defence, attacks):
		self.__hp = hp
		self.__attack = attack
		self.__defence = defence
		self.__atacks = attacks

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


##Honestly just a test for inheritance
class taxedermist(enemy):
	"""docstring for ClassName"""
	def __init__(self, hp , attack , defence , attacks, name):
		super(self.__class__, self).__init__(hp , attack , defence , attacks)
		self.name = name
		

