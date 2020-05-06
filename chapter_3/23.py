from modules import ch2_func

import re

text = ch2_func.extract_uk_text()
pattern = '(==+)(.*?)==+'
results = re.findall(pattern, text)

for i in results:
    level = i[0].count('=') - 1
    section_name = i[1]
    print('%d: %s' % (level, section_name))
