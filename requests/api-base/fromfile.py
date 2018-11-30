from xml.etree import ElementTree
#从硬盘的xml,以tree为ElementTree
tree = ElementTree.parse('t.xml')
tree = ElementTree.ElementTree(file='t.xml')
#获取根节点元素，root为Elemen
root = tree.getroot()
print(root)

with open('t.xml') as f:
    content = f.read()
root = ElementTree.fromstring(content)

for child in root:
    print(child.tag,child.attrib,child.text)
