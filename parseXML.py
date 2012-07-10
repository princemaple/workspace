import re

class node:
    def __init__(self, name, value):
        self.name=name
        self.value=value
        self.attrs={}
        self.children=[]

    def __call__(self):
        print "Tag Name: %s" %self.name
        print "Tag Value: %s" %self.value
        print "Tag attrs: %s" %self.attrs
        print "Children:",
        for child in self.children:
            print child.name,
        print
        print
        for child in self.children:
            child()

class root(node):
    def __call__(self):
        print "Tag Name: %s" %self.name
        print "Root Tag\n"
        for child in self.children:
            child()

def testchild(v):
    return v[0]=="<" and v[-1]==">"

def parse(f):
    rootname, rootvalue=re.findall("\<(\w+).*?\>(.*)\</\\1\>", f)[0]
    rootvalue=rootvalue.strip()
    rt=root(rootname, rootvalue)
    # print rootname
    # print rootvalue
    rt.children=furtherparse(rootvalue)
    return rt

def furtherparse(v):
    openclose=re.findall("\<(\w+)(.*?)\>(.*)\</\\1\>", v)
    selfclose=re.findall("\<(\w+)([\w\s\"=]*)\/\>", v)
    openclose.reverse()
    selfclose.reverse()
    children=[]
    while openclose or selfclose:
        if openclose and selfclose:
            if v.find(openclose[-1][0])<v.find(selfclose[-1][0]):
                current=openclose.pop()
                content=current[2].strip()
            else:
                current=selfclose.pop()
                content=0
        else:
            if openclose:
                current=openclose.pop()
                content=current[2].strip()
            else:
                current=selfclose.pop()
                content=0
        child=node(current[0], content or None)
        attrs=re.findall("(\w+)\s*\=\s*\"(\w+)\"", current[1].strip())
        for attrname, attrvalue in attrs:
            child.attrs[attrname]=attrvalue
        if content and testchild(content):
            child.children=furtherparse(content)
        children.append(child)
    return children

# def query(rt):
#     while 1:
#         q=raw_input("node name")


def main():
    f=raw_input("File name>>")
    xmlFile=open(f.strip(), "r").read().replace("\n", "").replace("\t","").strip()
    rt=parse(xmlFile)
    rt()
    # query(rt)
    raw_input()

main()
