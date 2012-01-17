
from mpoint import MPoint


def create_point_store():
	"""
	creates a new point_store
	"""
	point_store = { 'kept': 0, 'removed': 0 }
	return point_store
	

def unify_polygons(polygons, point_store):
	out = []
	for polygon in polygons:
		out.append(unify_polygon(polygon, point_store))
	return out


def unify_polygon(polygon, point_store):
	"""
	Replaces duplicate points with an instance of the 
	same point
	"""
	new_points = []
	for pt in polygon:
		if 'deleted' not in pt:
			pt = MPoint(pt[0], pt[1]) # eventually convert to MPoint
		pid = '%f-%f' % (pt.x, pt.y)
		if pid in point_store:
			point = point_store[pid]
			if point.three: point.deleted = True
			if point.two: point.three = True
			else: point.two = True
			point_store['removed'] += 1
		else:
			point = pt
			point_store['kept'] += 1
			point_store[pid] = pt
		new_points.append(point)
	return new_points

