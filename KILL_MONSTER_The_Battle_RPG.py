import threading
import random
import time
import os

#Monster design
class monster:
	def __init__(self, hp, attack):
		self.hp = hp
		self.attack = attack

attack_power = random.randint(2, 4)
dragon = monster(40, attack_power)
attack_status = False

#Character design
class character:
	def __init__(self, name, hp, attack, weapon):
		self.name = name
		self.hp = hp
		self.attack = attack
		self.weapon = weapon
		
warrior = character("WARRIOR", 10, 2, "Mystic Sword")
mage = character("MAGE", 15, 1, "Magic Wand")
dodge = False

#Screen clear
def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")

#Head
def game_title():
	print(" =•=•=•=•=•=•=•=•=•=•=")
	print(" >>> KILL MONSTER <<<")
	print(" ×× The Battle RPG ××")
	print(" =•=•=•=•=•=•=•=•=•=•=")

#Rules	
def game_instructions():
	print("\n BATTLE INSTRUCTIONS...\n")
	print(" >> For Attack → A + enter")
	print(" >> For Dodge  → D + enter")
	print("\n =•=•=•=•=•=•=•=•=•=•=")

#Live HP status		
def hp_status():
	print("\n ★ CURRENT HP STATUS...")
	print(f" >> {player.name} : {player.hp} HP")
	print(f" >> Dragon : {dragon.hp} HP")
	print("\n =•=•=•=•=•=•=•=•=•=•=")

#Player got hit or not
def show_status(message):
	clear_screen()
	game_title()
	hp_status()
	print(f"\n", message)

#Character Information	
def character_profile():
	print("\n YOUR CHARACTER PROFILE...\n")
	print(f" >> Character : {player.name}")
	print(f" >> Health    : {player.hp} HP")
	print(f" >> Attack    : {player.attack} HP")
	print(f" >> Weapon    : {player.weapon}")
	print("\n =•=•=•=•=•=•=•=•=•=•=")

#Character Selection	
game_title()
print("\n Select Your Character... ")
print(" >> Mage     → M + enter")
print(" >> Warrior  → W + enter")
chosen_character = input("\n Select: ").upper()

if chosen_character == "W":
	clear_screen()
	player = warrior
	game_title()
	time.sleep(0.5)
	character_profile()
	time.sleep(0.5)
	game_instructions()
	
elif chosen_character == "M":
	clear_screen()
	player = mage
	game_title()
	time.sleep(0.5)
	character_profile()
	time.sleep(0.5)
	game_instructions()
	
else:
	clear_screen()
	game_title()
	print("\n Invalid Selection!")
	exit()

#Continous Action of Dragon
def dragon_attack():
	global attack_status, dodge
	while player.hp > 0 and dragon.hp > 0:
		wait_time = random.randint(2,4)
		time.sleep(wait_time)
		
		attack_status = True
		print("\n DRAGON Attack Incoming!")
		time.sleep(0.6)
		
		if dodge == True:
			show_status(" Attack Dodged Successfully!")
		else:
			damage = random.randint(2,4)
			player.hp -= damage
			show_status("Oops! DRAGON Attacked!")
			
		attack_status = False
		dodge = False

#Continous Action of Player	
def player_action():
	global attack_status, dodge
	while player.hp > 0 and dragon.hp > 0:
		
		action = input(" >> ").upper()
		
		if action == "A":
			dragon.hp -= player.attack
		elif action == "D":
			if attack_status == True:
				dodge = True
		else:
			print(" Invalid Instruction!")

#Loading Animation
def loading():
	start_time = time.time()
	
	while time.time() - start_time < 5:
		for i in [" ", ".", "..", "..."]:
			print(f"\r >> Entering Battlefield{i}  ", end="")
			time.sleep(0.4)

#Start Game
time.sleep(0.5)
print("\n Click (S + enter) to Start The Battle!")
start = input("\n >> ").upper()

if start == "S":
	clear_screen()
	game_title()
	hp_status()
	print("")
	loading()
	
	clear_screen()
	game_title()
	hp_status()
	print("\n >> FIGHT!\n")
	
else:
	clear_screen()
	game_title()
	print("\n Try Again!\n You Typed Something else instead of 'S'\n\n GAME CLOSED!")
	exit()

#Threading part	
dragon_function = threading.Thread(target = dragon_attack)
player_function = threading.Thread(target = player_action, daemon = True)

dragon_function.start()
player_function.start()

dragon_function.join()


#Final Result Screen
clear_screen()
game_title()
hp_status()

if player.hp <= 0:
	print("\n GAME OVER!")
	print(f" The DRAGON killed {player.name}.")
	
elif dragon.hp <= 0:
	print("\n YOU WON!")
	print(f" The {player.name} killed DRAGON.")