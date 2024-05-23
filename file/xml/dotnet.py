# from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse(r"E:\1Web.config")
root = DOMTree.documentElement
COOSTR = root.getElementsByTagName("add")

for i in COOSTR:
    if i.getAttribute("name") == 'RedisConnectionString':
        print(i.getAttribute("connectionString"))
        i.setAttribute('connectionString', 'redis123456')
        print(i.getAttribute("connectionString"))
    # print(i.getAttribute("name"))
doc = xml.dom.minidom.Document()
with open(r"E:\2Web.config", 'w') as f:
    DOMTree.writexml(f, addindent='  ', encoding='utf-8')
