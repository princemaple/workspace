class LogicalSymbol(object):
	"""\
	To replace special marks by corresponding logical symbols

	@imply -> u'\u21d2'
	@unify -> u'\u2192'
	@biimp -> u'\u21d4'
	@equal -> u'\u2261'
	@conj  -> u'\u2227'
	@disj  -> u'\u2228'
	@xor   -> u'\u2295'
	@tauto -> u'\u22a4'
	@contr -> u'\u22a5'
	@univs -> u'\u2200'
	@exist -> u'\u2203'
	@consq -> u'\u22a8'\
	"""
	def __init__(self, context=None):
		super(LogicalSymbol, self).__init__()
		self.content = context
		self.__data = {
			"@imply" : u' \u21d2 ',
			"@unify" : u' \u2192 ',
			"@biimp" : u' \u21d4 ',
			"@equal" : u' \u2261 ',
			"@not"   : u' \u00ac',
			"@conj"  : u' \u2227 ',
			"@disj"  : u' \u2228 ',
			"@xor"   : u' \u2295 ',
			"@tauto" : u'\u22a4',
			"@contr" : u'\u22a5',
			"@univs" : u'\u2200',
			"@exist" : u'\u2203',
			"@consq" : u' \u22a8 '
		}
		self.result = None

	def read(self, context):
		self.content = context
		self.result = None

	def readfile(self, path):
		f = open(path, "r")
		self.content = f.read()
		f.close()
		self.result = None

	def process(self, context = None):
		if context: self.read(context)
		if not self.content: return None
		import re
		processed = self.content
		for symbol in self.__data:
			processed = re.sub(" *"+symbol+" *",
				self.__data[symbol], processed)
		self.result = processed
		return processed

	def htmlize(self):
		template = """<!doctype html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<title>LogicalSymbol Process Result</title>\n</head>\n<body>\n\t<div style="width:800px; margin: auto;">{{content}}</div>\n</body>\n</html>"""
		if not self.result: self.process()
		return template.replace("{{content}}",
			self.result and self.result.replace("\n", "<br>") or "None")

	def dump(self):
		f = open("LogicalSymbolDump.html", "wb")
		f.write(self.htmlize().encode("utf8"))
		f.close()
