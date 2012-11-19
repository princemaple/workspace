# coding=utf-8

import re

class LogicalSymbol(object):
	"""\
	To replace special marks by corresponding logical symbols

	@imply -> u'\u21d2' ⇒
	@unify -> u'\u2192' →
	@biimp -> u'\u21d4' ⇔
	@equal -> u'\u2261' ≡
	@not   -> u'\u00ac' ¬
	@conj  -> u'\u2227' ∧
	@disj  -> u'\u2228' ∨
	@xor   -> u'\u2295' ⊕
	@tauto -> u'\u22a4' ⊤
	@contr -> u'\u22a5' ⊥
	@univs -> u'\u2200' ∀
	@exist -> u'\u2203' ∃
	@consq -> u'\u22a8' ⊨
	@empty -> u'\u2205' Ø
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
			"@tauto" : u' \u22a4 ',
			"@contr" : u' \u22a5 ',
			"@univs" : u'\u2200',
			"@exist" : u'\u2203',
			"@consq" : u' \u22a8 ',
			"@empty" : u' \u2205 '
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

	def de_utf8(self):
		"""
		If input string/file is in UTF-8 coding,
		it has to be decoded into ascii.
		"""
		self.content = self.content.decode("utf8")

	def process(self, context = None):
		if context: self.read(context)
		if not self.content: return None
		processed = self.fromRaw(self.content)
		for symbol in self.__data:
			try:
				processed = re.sub(" *"+symbol+" *",
					self.__data[symbol], processed)
			except:
				print("Expecting ascii input")
				raw_input()
				return None
		self.result = processed
		return processed

	def fromRaw(self, content):
		data = [
			(r"<=>",  "@biimp"),
			(r"=>" ,  "@imply"),
			(r"->" ,  "@unify"),
			(r"<\+>", "@xor"),
			(r"~"  ,  "@not"),
			(r"\ball\b",  "@univs"),
			(r"\bany\b",  "@exist"),
			# ("\band\b",  "@conj"),
			# ("\bor\b",   "@disj"),
			(r"\{\}", "@empty")
		]
		for pair in data:
			content = re.sub(pair[0], pair[1], content)
		return content

	def htmlize(self):
		template = """<!doctype html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<title>LogicalSymbol Process Result</title>\n</head>\n<body>\n\t<div style="width:800px; margin: auto;">{{content}}</div>\n</body>\n</html>"""
		if not self.result: self.process()
		return template.replace("{{content}}",
			self.result and self.result.replace("\n", "<br>") or "None")

	def dump(self):
		f = open("LogicalSymbolDump.html", "wb")
		f.write(self.htmlize().encode("utf8"))
		f.close()
