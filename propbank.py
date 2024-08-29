import re
import xml.etree.ElementTree as ET

# 解析XML文件
tree = ET.parse('./abandon.xml')
root = tree.getroot()

# 查找所有roleset元素并提取name属性值
specific_id = "abandon.01"
roleset = root.find(f".//roleset[@id='{specific_id}']")
if roleset is not None:
    name = roleset.get('name')
    print(name)
else:
    print(f'roleset with id="{specific_id}" not found')
line = "example_concept-01\n :ARG1-of"
idx=re.search(r'-(\d{2})',line).group(1)
concept = line[:re.search('-[0-9][0-9]', line).start()]# list[:7]切片前半部分，在这里是去掉-01；search查找第一个匹配项
concept = concept.split('/ ')[0].strip()
print(idx)  # 输出：example_concept
