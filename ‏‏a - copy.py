class Udacian():
	"""this class contains to store movie """
	def __init__(self, name,city,erollment,nanodegree,status):
		self.name = name
		self.city = city
		self.erollment = erollment
		self.nanodegree = nanodegree
		self.status=status
		
Udacian_obj=Udacian('ahmed','taif','sdf','fullstack','student')
print (Udacian_obj.name)