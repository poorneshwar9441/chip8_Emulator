

class Keyboard(object):
	def __init__(self):
		self.dic = {
		 
		} #keyboard dictnory 

		self.mapping = { 
		} 

		for i in range(15):
			self.dic[i] = False

	


	def __str__(self):
		return f"Keyboard values : {self.dic}"

