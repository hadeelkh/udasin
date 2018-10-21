class Udacian():
	"""this class contains to store movie """
	def __init__(self, name,city,erollment,nanodegree,status):
		self.name = name
		self.city = city
		self.erollment = erollment
		self.nanodegree = nanodegree
		self.status=status
	def show_city(self):
		print self.city
		
Udacian_obj=Udacian('ahmed','taif','sdf','fullstack','student')
Udacian_obj.show_city()