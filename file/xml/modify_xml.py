import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse(r"aa.xml")
# 取得根的值
root = DOMTree.documentElement
print(root)
# 如果根里面包含shelf就打印出来
if root.hasAttribute("shelf"):
    print("Root element : %s" % root.getAttribute("shelf"))
# 搜索节点包含名字node
nodes = root.getElementsByTagName("node")
for node in nodes:
    if node.hasAttribute("title"):
        print("节点 element : %s" % node.getAttribute("title"))
    date = node.getElementsByTagName('date')[0]
    print("Type: %s" % date.childNodes[0].data)
    description = node.getElementsByTagName('description')[0]
    print("description: %s" % description.childNodes[0].data)
# 搜索节点包含名字attribute
nodes = root.getElementsByTagName("attribute")
for node in nodes:
    if node.getAttribute("key") == 'KEY1':
        print("未修改的value值为" + node.getAttribute("value"))
    elif node.getAttribute("key") == 'KEY2':
        node.setAttribute('value', 'change VALUE2')
        print("修改后的value值为" + node.getAttribute("value"))
# 保存修改后的内容到文件
with open(r"bb.xml", 'w') as f:
    DOMTree.writexml(f, addindent='  ', encoding='utf-8')
