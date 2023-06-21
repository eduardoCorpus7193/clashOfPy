class Character:
	name = "char"
	hp = 100
	strenghts = "strenghts"
	weaknesses = "weaknesses"
	currentHP = 100
	atkPoints = 0

	def __init__(self, name, hp, strenghts, weaknesses, currentHP, atkPoints):
		self.name = name
		self.hp = hp
		self.strenghts = strenghts
		self.weaknesses = weaknesses
		self.currentHP = currentHP
		self.atkPoints = atkPoints

	def identify(self):
		print("Name:", self.name, "HP:", self.hp, "Strenghts:", self.strenghts, "Weaknesses:", self.weaknesses, "Attack points: ", self.atkPoints)

	def attack(self, other):
		print(self.name, "is attacking to", other.name, "HP before attack:", other.currentHP)
		other.currentHP = other.currentHP - self.atkPoints
		if other.currentHP <= 0:
			other.currentHP = 0
		print(other.name, "HP after attack ", other.currentHP)

validate = True
while validate == True:
	while True:
	    try:
	    	optionOne = int(input("\nSelect the first character: \n1.-Wizard(magic)\n2.-Giant(melee)\n3.-Hunter(fire arm)"))
	    	if(optionOne!=1 and optionOne!=2 and optionOne!=3):
	    		print("\nOops!  That was no valid option.  Try again...")
	    	else:	
	    		break
	    except ValueError:
	        print("\nOops!  That was no valid option.  Try again...")

	#Creating first character
	if(optionOne == 1):
		#Creating wizard
		char1 = Character("Wizard", 80, "Firearm", "Melee", 80, 23)
		print("\nFirst player is: ")
		char1.identify()
		print("\n")

	if(optionOne == 2):
		#Creating giant
		char1 = Character("Giant", 120, "Magic", "Firearm", 120, 28)
		print("\nFirst player is: ")
		char1.identify()
		print("\n")

	if(optionOne == 3):
		#Creating Hunter
		char1 = Character("Hunter", 100, "Melee", "Magic", 80, 21)
		print("\nFirst player is: ")
		char1.identify()
		print("\n")

	while True:
		try:
			optionTwo = int(input("\nSelect the second character char: \n1.-Wizard(magic)\n2.-Giant(melee)\n3.-Hunter(fire arm)"))
			if(optionTwo!=1 and optionTwo!=2 and optionTwo!=3):
				print("\nOops!  That was no valid option.  Try again...")
			else:	
	 			break
		except ValueError:
			print("\nOops!  That was no valid option.  Try again...")

	#Creatin second character
	if(optionTwo == 1):
		#Creating wizard
		char2 = Character("Wizard", 80, "Firearm", "Melee", 80, 23)
		print("\nSecond player is: ")
		char2.identify()
		print("\n")

	if(optionTwo == 2):
		#Creating giant
		char2 = Character("Giant", 120, "Magic", "Firearm", 120, 28)
		print("\nSecond player is: ")
		char2.identify()
		print("\n")

	if(optionTwo == 3):
		#Creating Hunter
		char2 = Character("Hunter", 100, "Melee", "Magic", 80, 21)
		print("\nSecond player is: ")
		char2.identify()
		print("\n")

	#start the turns
	turn = 1

	while char1.currentHP>0:
		if char2.currentHP>0:
			if turn%2==1:
				turn += 1
				char1.attack(char2)
				if char2.currentHP<=0:
					print(char1.name, "wins")
					break
			else:
				turn += 1
				char2.attack(char1)
				if char1.currentHP<=0:
					print(char2.name, "wins")
					break

	sino = input("\nDo you want to play again? y/n")
	if sino != "y":
		validate = False
print("\nThank you for playing ")