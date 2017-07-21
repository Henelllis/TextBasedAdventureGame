import os
import sys
import ConfigParser
from enemy import enemy,taxedermist

def main():
		BadDude = enemy(1,1,1,1)
		print BadDude.get_hp()
		BadDude.set_hp(20)
		print BadDude.get_hp()
		taximan = taxedermist(34,1,1,1,'Taxerdermist')
		print taximan.get_hp()
		print 'Works'



if __name__ == "__main__":
	print 'Hello Globe'
	main()