

class Keyboard(object):
	def __init__(self):
		self.dic = {0 : False,1:False,
		 2:False,
		 3:False,
		 4:False,
		 5:False,
		 6:False,
		 7:False,
		 8:False,
		 9:False,
		 10:False,
		 11:False,
		 12:False,
		 13:False,
		 14:False,
		 15:False
		} #keyboard dictnory 

		self.mapping = { 
		} 


	def __str__(self):
		return f"Keyboard values : {self.dic}"

