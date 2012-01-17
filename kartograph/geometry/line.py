
from bbox import BBox
from geometry import Geometry


class Line(Geometry):
	"""
	simple line (= list of points)
	"""
	def __init__(self, points):
		self.points = points
		
	def bbox(self):
		"""
		returns the bounding box of the line
		"""
		bbox = BBox()
		for pt in self.points:
			bbox.update(pt)
		return bbox
	
	
	def project(self, proj):
		"""
		projects the line to a map projection
		"""
		pts = []
		for pt in self.points:
			p = proj.project(pt[0], pt[1])
			if p is not None:
				pts.append(p)
		return Line(pts)
	
	
	def project_view(self, view):
		"""
		transforms the line to a new view
		"""
		pts = []
		for pt in self.points:
			p = view.project(pt)
			pts.append(p)
		return Line(pts)
		
	
	def to_svg(self, round):
		"""
		constructs a svg representation of this line
		"""
		from svgfig import SVG
		path_str = ""
		if round is False: fmt = '%f,%f'
		else: 
			fmt = '%.'+str(round)+'f'
			fmt = fmt+','+fmt
			
		for pt in self.points:
			if path_str == "": path_str = "M"
			else: path_str += "L"
			path_str += fmt % pt
			
		path = SVG('path', d=path_str)
		return path
		
	
	def is_empty(self):
		return len(self.points) == 0
		
	
	def unify(self, point_store):
		from kartograph.simplify import unify_polygon
		self.points = unify_polygon(self.points, point_store)

	
	def points(self):
		return [self.points]
		
		