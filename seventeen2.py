import random


def human(line1):
	total_marbles = 17
	list1 = []
	list1 = line1.split(',')
	
	final_str = ""
	player = ""
	human_marbles = 0
	i = 0
	for i in list1:
		
		try:
			#human_marbles =int(raw_input("How many marbles do you want to remove (1-3) ?"))
			human_marbles = int(i)
		except ValueError:
			continue

		else:
			if (human_marbles < 1) or (human_marbles > 3) :
					#print "This is not a valid option. Try again. \n Number of marbles left in jar : {0}".format(total_marbles)
				continue
			else:
				pass
			if human_marbles < total_marbles:
				total_marbles = total_marbles - human_marbles
				final_str+= "-"+str(human_marbles)
			else: 
							
				player = "P2"
				return [final_str,player]
						
			if human_marbles < total_marbles:
				total_marbles = total_marbles - human_marbles
				final_str+= "-"+str(human_marbles)
			else:
						
							
				player = "P1"
				return [final_str,player]
	
			
def main():
	game_number = 1
	final_list = []
	with open("output.txt","w") as fout:
		with open("i206_placein_input_0.txt","r") as fin:
			for line in fin:
				
				final_list=human(line.strip())
				fout.write("Game #"+str(game_number)+". Play Sequence:"+final_list[0][1:]+". Winner:"+final_list[1]+"\n")
				game_number+= 1


main()
	