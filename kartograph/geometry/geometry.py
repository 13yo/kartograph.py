

		
class Geometry:
	"""
	base class for all geometry
	"""
	def project(self, proj):
		"""
		project geometry
		"""
		raise NotImplementedError('project() is not implemented')
	
	def bbox(self):
		raise NotImplementedError('bbox() is not implemented')
		
	def project_view(self, view):
		raise NotImplementedError('project_view() is not implemented')

	
class SolidGeometry(Geometry):
	"""
	base class for all solid geometry, e.g. polygons
	"""
	def area():
		"""
		calculates area for this geometry
		"""
		raise NotImplementedError('area() is not implemented')
		
	def centroid():
		"""
		calculates centroid for this geometry
		"""
		raise NotImplementedError('centroid() is not implemented')
	
	def invalidate(self):
		self.__area = None