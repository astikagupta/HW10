import random


def human():
	total_marbles = 17
	while (total_marbles > 0):
		try:
			human_marbles =int(raw_input("How many marbles do you want to remove (1-3) ?"))

		except ValueError:
			print "Invalid input. Try again."

		else:
			if (human_marbles < 1) or (human_marbles > 3) or (human_marbles > total_marbles):
				print "This is not a valid option. Try again. \n Number of marbles left in jar : {0}".format(total_marbles)
				continue
			else:
					total_marbles = total_marbles - human_marbles
					print "You removed {0} marbles.\n Number of marbles left in jar : {1}".format(human_marbles,total_marbles)
					if total_marbles == 0:
						print "There are no marbles left. Computer wins."
						break
					if human_marbles <= total_marbles:
						computer_marbles = human_marbles
					else:
						computer_marbles = random.randint(1,total_marbles)
					total_marbles = total_marbles - computer_marbles
					print "Computer's turn...\n Computer removed {0} marbles.\n Number of marbles left in jar : {1}".format(computer_marbles,total_marbles)
					if total_marbles == 0:
						print "There are no marbles left. You win."
						break
			
def main():
	human()

main()
	