class gameProperty:

	def __init__(self, name, board_position, price):
		self.board_position = board_position
		self.price = price
		self.startSpace = 0
		self.name = name

	def getPrice(self):
		return self.price

	def getPosition(self):
		return self.board_position

	def getName(self):
		return self.name
	



	
