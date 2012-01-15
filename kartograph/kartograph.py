
from options import parse_options
from layersource import handle_layer_source

class Kartograph(object):
	"""
	main class of Kartograph
	"""
	def __init__(self):
		pass
		
	def generate(self, opts, outfile=None):
		"""
		generates svg map
		"""
		parse_options(opts)
		self.prepare_layers(opts)
		lon0,lat0 = self.get_map_center(opts)
		print lon0,lat0
		# print opts	
		
			
	def prepare_layers(self, opts):
		"""
		prepares layer sources
		"""
		self.layers = layers = {}
		for layer in opts['layers']:
			id = layer['id']
			src = handle_layer_source(layer['src'])
			layers[id] = src
			
					
	def get_map_center(self, opts):
		"""
		depends on the layer config
		"""
		
		return (0,0)
		
	def get_layer_center(self, layer):
		
	
	
	def get_bounds(self, opts, proj):
		"""
		computes the (x,y) bounding box for the map, given a specific projection
		"""
		bnds = opts['bounds']
		type = bnds['type']
		data = bnds['data']
		
		if bt == "bbox": # catch special case bbox
			bt = "points"
			lon0,lat0,lon1,lat1 = data # lon0,lat0,lon1,lat1
			data = [(lon0,lat0),(lon0,lat1),(lon1,lat0),(lon1,lat1)]
		
		bbox = Bounds2D()
				
		if bt == "points":
			for lon,lat in data:
				pt = proj.project(lon,lat)
				bbox.update(pt)
				
		if bt == "polygons":
			data['layer'] = 'countries'
			data['idcol'] = 'ISO3'
			data['ids'] = ['DEU','FRA','ESP']
			
		
		return bbox
	
