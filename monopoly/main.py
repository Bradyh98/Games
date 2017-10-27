from player import Player
from gameProperty import gameProperty
from random import randint
arr_players = []
arr_tiles = []
num_players = -1
GO  = gameProperty("GO", 0, 0)
brown1 = gameProperty("Meditteranian Avenue", 1, 60)
brown2 = gameProperty("Baltic Avenue", 3, 60)
light_blue1 = gameProperty("Oriental Avenue", 6, 100)
light_blue2 = gameProperty("Vermont Avenue", 8, 100)
light_blue3 = gameProperty("Connecticut Avenue", 9, 120)
purple1 = gameProperty("St. Charles Place", 11, 140)
purple2 = gameProperty("States Avenue", 13, 140)
purple3 = gameProperty("Virginia Avenue", 14, 160)
orange1 = gameProperty("St. James Place", 16, 180)
orange2 = gameProperty("Tennessee Avenue", 18, 180)
orange3 = gameProperty("New York Avenue", 19, 120)
red1 = gameProperty("Kentucky Avenue", 21, 220)
red2 = gameProperty("Indiana Avenue", 23, 220)
red3 = gameProperty("Illinois Avenue", 24, 240)
yellow1 = gameProperty("Atlantic Avenue", 26, 260)
yellow2 = gameProperty("Ventnor Avenue", 27, 260)
yellow3 = gameProperty("Marvin Gardens", 29, 280)
green1 = gameProperty("Pacific Avenue", 31, 300)
green2 = gameProperty("North Carolina Avenue", 32, 300)
green3 = gameProperty("Pennsylvania Avenue", 34, 320)
blue1 = gameProperty("Park Place", 37, 350)
blue2 = gameProperty("Boardwalk", 39, 400)
rr1 = gameProperty("Reading Railroad", 5, 200)
rr2 = gameProperty("Pennsylvania Railroad", 15, 200)
rr3 = gameProperty("B&O Railroad", 25, 200)
rr4 = gameProperty("Short Line", 35, 200)
income_tax = gameProperty("Income Tax", 4, 200)
luxury_tax = gameProperty("Luxury Tax", 38, 200)
community_chest1 = gameProperty("Community Chest", 2, 0)
community_chest2 = gameProperty("Community Chest", 17, 0)
community_chest3 = gameProperty("Community Chest", 33, 0)
chance1 = gameProperty("Chance", 7, 0)
chance2 = gameProperty("Chance", 22, 0)
chance3 = gameProperty("Chance", 36, 0)
jail = gameProperty("Jail", 10, 0)
electric_company = gameProperty("Electric Company", 12, 150)
water_works = gameProperty("Water Works", 28, 150)
free_parking = gameProperty("Free Parking", 20, 0)
go_to_jail = gameProperty("Go To Jail", 30, 0)
# fill array of tiles #
arr_tiles.append(GO)
arr_tiles.append(brown1)
arr_tiles.append(community_chest1)
arr_tiles.append(brown2)
arr_tiles.append(income_tax)
arr_tiles.append(rr1)
arr_tiles.append(light_blue1)
arr_tiles.append(chance1)
arr_tiles.append(light_blue2)
arr_tiles.append(light_blue3)
arr_tiles.append(jail)
arr_tiles.append(purple1)
arr_tiles.append(electric_company)
arr_tiles.append(purple2)
arr_tiles.append(purple3)
arr_tiles.append(rr2)
arr_tiles.append(orange1)
arr_tiles.append(community_chest2)
arr_tiles.append(orange2)
arr_tiles.append(orange3)
arr_tiles.append(free_parking)
arr_tiles.append(red1)
arr_tiles.append(chance2)
arr_tiles.append(red2)
arr_tiles.append(red3)
arr_tiles.append(rr3)
arr_tiles.append(yellow1)
arr_tiles.append(yellow2)
arr_tiles.append(water_works)
arr_tiles.append(yellow3)
arr_tiles.append(go_to_jail)
arr_tiles.append(green1)
arr_tiles.append(green2)
arr_tiles.append(community_chest3)
arr_tiles.append(green3)
arr_tiles.append(rr4)
arr_tiles.append(chance3)
arr_tiles.append(blue1)
arr_tiles.append(luxury_tax)
arr_tiles.append(blue2)

# Start Program #
def printBoard():
	for i in range(0,10):
		for j in range(0,10):
			if i == 0 and j == 9:
				print ("[ ]")
			elif i == 0 and j != 9:
				print ("[ ]", end='')
			elif i == 9 and j == 9:
				print ("[ ]")
			elif i == 9 and j != 9:
				print ("[ ]", end='')
			elif j == 0 or j == 9:
				print ("[ ]")
			elif j == 8:
				print ("", end='')
			else:
				print ("    ", end='')

def rollDice():
	return randint(1,6)

			
num_players = int(input("How many players?"))
while ((num_players < 2) or (num_players > 4)):
	print ("Number of players can only be between 2 and 4!!!\n try again")
	num_players = input("How many players?\n")

player1 = Player("Anthony", 1500, 0)
arr_players.append(player1)


printBoard()
while (input("Enter anything but (N) to roll dice (N quits game)").upper() != "N"):
	add1 = rollDice()
	print ("Your first roll is: " + str(add1))
	add2 = rollDice()
	print ("Your second roll is: " + str(add2))
	player1.setPosition(add1 + add2)
	print (player1.getPosition())
	yes_no = input("Would you like to buy: " + str(arr_tiles[player1.getPosition()].getName()) +" for $" + str(arr_tiles[player1.getPosition()].getPrice()) + " (Y for yes, N for no)")
	if yes_no == "Y":
		player1.buyProperty(True, arr_tiles[player1.getPosition()].getPrice())
		print ("You just bought: " + str(arr_tiles[player1.getPosition()].getName()))
		print ("Your balance is: " + str(player1.getBalance()))
	



