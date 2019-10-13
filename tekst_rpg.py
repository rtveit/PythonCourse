class Player:
	health = 10
	attack = 3
	defense = 1
	level = 1
	isShielding = False

	def __init__(self, name):
		self.name = name

	def hit(self, target):
		target.health = target.health - self.attack
		print(self.name + " gjorde " + str(self.attack) + " skadepoeng" + "på Troll")
		print("Motstanderen har " + str(target.health) + " liv igjen")

	def shield(self):
		self.isShielding = True
		print(self.name + " blokkerer neste angrep")

class Troll:
	health = 6
	attack = 2

	def hit(self, target):
		if target.isShielding == True:
			print("Player is Shielding! ")
			target.health = target.health - (self.attack - target.defense)
		
		elif target.isShielding == False: 
			target.health = target.health - self.attack
		print(target.name + " tok " + str(self.attack) + " skadepoeng")
		print(target.name + " har " + str(target.health) + " livspoeng igjen")

class Boss:
	health = 50
	attack = 5
	hasAttacked = False

	def hit(self, target):
		target.health = target.health - self.attack
		print(self.name + " gjorde " + str(self.attack) + " skadepoeng" + "på Troll")
		print("Motstanderen har " + str(target.health) + " liv igjen")


def main():
	print("Velkommen til Tekstbasert RPG")
	print("Skriv inn spillernavn: ", end="")
	playerName = input()
	print("Hei " + playerName + " velkommen til en verden fylt av troll")
	
	player = Player(playerName) 

	print("Du begynner disse verdiene")
	print("Livspoeng: " + str(player.health))
	print("Angrepspoeng: " + str(player.attack))

	troll = Troll()
	print("Du har nå møtt et troll!")

	isGameRunning = True

	while isGameRunning == True:
		print("Du har nå to valg: hit og shield")
		choice = input()
		
		if choice == "hit":
			player.hit(troll)
		elif choice == "shield":
			player.shield()

		troll.hit(player)

		if troll.health <=0:
			isGameRunning = False
			print(" Grattis Du er nå en banemann ")
			player.level = player.level + 1
			player.health = player.health + 10
			player.attack = player.attack + 4
			player.defense = player.defense + 2
			print("Du har nå Level 2 og har fått i +10 health +4 attack +2 defense")
			print (playerName + " har nå I health " + str(player.health) )

		elif player.health <=0:
			isGameRunning = False
			print(" Da kan du hvile ")
			print("Spillet er over ")
			break
			
	


if __name__ == "__main__":
	main()