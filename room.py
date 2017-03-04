print("Available commands include: 'lantern','look','eat','drink','pray','love' and 'quit'")

import random
x=0
y=0
thirst=0
L=[]
dark = True
full = False
while True:

#Easter egg processing
	if len(L)==3:
		if L==[1,2,3]:
			print("This is supposed to be a scary dungeon! What is with all the feasting and sitting around?")
			L=[]
		elif L==[1,2,1]:
			L=[1]
		else:
			L=[]
	elif len(L)==2:
		if L==[1,1]:
			L=[1]
		elif L!=[1,2]:
			L=[]
	elif len(L)==1:
		if L!=[1]:
			L=[]
#Darkness resolution
	if dark == True:
		print('It is dark.')
	else:
		x=random.randint(0,4)
		if x==0:
			dark=True
			print("Your lantern has been extinguished by a spooky breeze!")
#thirst counting and input
	if thirst==3:
		print("You are thirsty.")
	elif thirst==6:
		print("You just died of dehydration...")
		break
	cmd = input('? ')
	thirst=thirst+1	

#cmd resolution	
	if cmd == 'eat':
		if full==False:
			print('Nom nom nom.')
			full=True
		else:
			print("You can't bring yourself to eat another bite.")
			full=False
		L.append(1)
	elif cmd == 'drink':
		print('Glug glug glug *burp*')
		thirst=0
		L.append(4)
	elif cmd == 'look':
		if dark == True:
			print('Did I mention that it was dark?')
		else:
			print('You are in a maze of twisty little passages, all alike.')
		L.append(4)
	elif cmd == 'lantern':
		print('You are enlightened.')
		dark = False
		L.append(4)
	elif cmd == "pray":
		print("You try to focus on prayer despite this sudden text filled adventure that has become your life.")
		L.append(2)
	elif cmd == "love":
		print("Your love and positivity flows outwards from you... it has no effect.")
		L.append(3)
	elif cmd == 'quit':
		break
	else:
		L.append(4)
		print("I don't know that command.")
