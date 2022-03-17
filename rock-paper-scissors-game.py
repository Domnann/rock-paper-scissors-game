import random

def start_game():
	print ('Play Rock Paper Scissors: r for Rock, p for Paper, s for Scissors, stop to end game')
	while True:
		irounds= input('How many rounds would you like to play: ')
		if irounds.lower() == ("stop"):
			print("game ended by player")
			quit()
		try:
			rounds = int(irounds)			
			break
		except:
			print ("Invalid Input! Try again")
			continue
	count= 0
	user_score = 0
	computer_score = 0
	while True:
		if rounds == (count):
			break
		print ("Round ", count+1)
		user= input("Enter Choice:")
		user_= str(user)
		user_play = user_.lower()
		if user_play == ("stop"):break
		computer_play = random.choice(['r', 'p', 's'])
		
		if user_play == computer_play:
			count = count + 1
			print('computer played:',computer_play)
			print ('Urrgh, tie game!!!')
		elif (user_play== "r" and computer_play == "s") or ( user_play == "s" and computer_play== "p") or (user_play == "p" and computer_play=="r" ):
			print('computer played:',computer_play)
			print ("Congrats,you won!!!")
			count = count + 1
			user_score = user_score +1
		elif (user_play== "r" and computer_play == "p") or ( user_play == "s" and computer_play== "r") or (user_play == "p" and computer_play=="s" ):
			print('computer played:',computer_play)
			print ("Sorry, you lost")
			count = count + 1
			computer_score = computer_score + 1
		elif (user_play != "r" or "p" or "s"):
			print ("Invalid input, Try again:")
			continue
	if user_score > computer_score:
		print ("\nGreat job!!! \nYour score is {}, computer's score is {}".format(user_score, computer_score) )
	elif user_score < computer_score:
		print ("\nToo bad, you lost! \nYour score is {}, computer's score is {}".format(user_score, computer_score) )
	else:
		print ("\nWow, it's a draw \nYour score is {}, computer's score is {}".format(user_score, computer_score) )

if __name__== "__main__":
    start_game()
