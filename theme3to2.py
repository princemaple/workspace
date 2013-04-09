import re

with open("XDefault.sublime-theme", "r") as f:
	t = f.read().replace("\n", "@")
	s = "// transient property not needed"
	t = re.sub(r"\{[^{]+?transient.+?\},", s, t)
	t = t.replace("@", "\n")
	f.write(t)
	f.close()
