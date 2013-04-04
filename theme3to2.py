import re

with open("XDefault.sublime-theme", "r") as f:
	w = open("XDefault2.sublime-theme", "w")
	t = f.read().replace("\n", "@")
	s = "// transient property not needed"
	t = re.sub(r"\{[^{]+?transient.+?\},", s, t)
	t = t.replace("@", "\n")
	w.write(t)
	w.close()
