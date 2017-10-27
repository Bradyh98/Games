class Player:
	#Constructors
	
	def __init__(self, name, money_balance, position):
		self.name = name
		self.money_balance = money_balance
		self.position = position

	# Start Methods #
	def deposit(self, amount):
		self.money_balance = self.money_balance + amount

	def withdraw(self, amount):
		self.money_balance = self.money_balance - amount

	def getBalance(self):
		return self.money_balance

	def setPosition(self, num_spaces):
		self.position = self.position + num_spaces

	def getPosition(self):
		return self.position

	def buyProperty(self, bool_buy, price):
		self.bool_buy = bool_buy
		self.money_balance = self.money_balance - price


	#def buyProperty(self, price):


