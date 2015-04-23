
# user-agent randomizer

"""
from random import randint

patch = 'user-agent.list'
i = 0
f = open(patch, 'r')
for line in f:
    i += 1
f.close()
line_number = randint(0, i-1)
f = open(patch, 'r')
tmp = f.readlines()[line_number]
f.close()
if '\n' in tmp:
    tmp = tmp.replace('\n', '')
elif '\r' in tmp:
    tmp = tmp.replace('\r', '')
print(tmp)
"""

import markup

items = ("Item one", "Item two", "Item three", "Item four")
paras = ("This was a fantastic list.", "And now for something completely different.")
images = ("thumb1.jpg", "thumb2.jpg", "more.jpg", "more2.jpg")

page = markup.page()
page.init(title="My title", css=('one.css', 'two.css'), header="Something at the top", footer="The bitter end.")
page.ul(class_='mylist')
page.li(items, class_='myitem')
page.ul.close()
page.p(paras)
page.img(src=images, width=100, height=80, alt="Thumbnails")

print page

f = open('1.html', 'w')
f.write(str(page))
f.close()