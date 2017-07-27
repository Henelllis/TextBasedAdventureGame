import os
import sys
import ConfigParser
import cmd
from enemy import enemy,taxedermist
from character import character


#character = None

#def start_Character(name):
#	global character 
#	character = character(name)
def global_counter(): 
	global counter
	counter = 0
	
	
class AttackChoiceShell(cmd.Cmd):
	intro = '\n\n\n'
	prompt = 'hit <- hit\n tic <-tickle\n'
	file = None
	
	def __init__(self):
		cmd.Cmd.__init__(self)
		self.__damage = 0
	

		
	def do_a(self,line):
		'attacking with hit for 1 damage'
		self.__damage = 1
		return 1
		
	def do_EOF(self, line):
		return True
	
	def postcmd(self, stop, line):
		print 'postcmd(%s, %s)' % (stop, line)
		return cmd.Cmd.postcmd(self, stop, line)
	
	def get_damage(self):
		return self.__damage
		

class BattleShell(cmd.Cmd, enemy):
	intro = 'TIME TO BATTLEEEEEEEEEEEEEEEEEEEEEE'
	prompt = 'a <- attack\n e <- enemy statistic\n'
	file = None
	
	def __init__(self, enemy):
		cmd.Cmd.__init__(self)
		self.enemy = enemy
		
	def do_a(self, line):
	
		print('attack enemy')
		attackShell =  AttackChoiceShell()
		damage = attackShell.cmdloop()
		#damage = 
		self.enemy.set_hp(self.enemy.get_hp() - attackShell.get_damage() )
		
		if(self.enemy.get_hp() <= 0):
			print 'enemy has vanquisd the battle is over'
			return True
		else:
			pass
			
		
	def do_e(self, line):
		print '**************************'
		print  str(self.enemy.get_name()) + ' : ' + str(self.enemy.get_hp()) + '/' + str(self.enemy.get_curhealth())
		print '**************************'
		
		
	def do_exit(self, *args):
		print('Battle Finished')
		return True
		
	def do_EOF(self, line):
		return True
	
		
		
	

def main():
	global_counter()
	print 'Hello New Player\n '

	player_name = raw_input('what''s your name??')

	print('Welcome %s ' % player_name)
	
	#	start_Character(player_name)

	#print('You''re charachters name is ' + player_name.get_name())

	taximan = taxedermist(34,1,1,1,'Taxerdermist')
	boolean = BattleShell(taximan).cmdloop()
	print('This boolean be ' + str(boolean))
	
	print taximan.get_hp()
	#	battle(taximan)
	print 'Works'
	
	

def print_enemy_statistic(enemy):
	print '**************************'
	print  str(enemy.get_name()) + ' : ' + str(enemy.get_curhealth()) + '/' + str(enemy.get_hp())
	print '**************************'

def battle_options():

	invalid_response = True

	while(invalid_response):
		print '++++++++++++++++++++++++++++++++'
		print 'What would you like to do in this battle'
		print 'A: attack'
		print 'E: get Enemy Info'
		print 'I: get Inventory information'
		print '++++++++++++++++++++++++++++++++'
		response = raw_input()
		if(response in ['a','A','e','E', 'i', 'I']):
			return response
		else:
			print response + ' is invalid please pick another choicce'

def run_option(option ,enemy):
	if option in ['e','E']:
		print_enemy_statistic(enemy)
	elif option in ['a','A']:
		pass


def battle(enemy):
	print 'You are now battling ' + enemy.get_name()
	
	is_battle_running = True

	while(is_battle_running):
		option = battle_options()
		run_option(option, enemy)
		break



if __name__ == "__main__":

	main()