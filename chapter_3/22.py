from modules import ch2_func

import re

text = ch2_func.extract_uk_text()
pattern = '\[\[Category:(.*?)(?:\|.*)?\]\]'
results = re.findall(pattern,text)

for i in results:
  print(i)