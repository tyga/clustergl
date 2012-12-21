#!/usr/bin/python

import urllib
from lxml import html

# f = urllib.urlopen("http://www.opengl.org/sdk/docs/man/xhtml/glGet.xml")
f = urllib.urlopen("http://www.opengl.org/sdk/docs/man2/xhtml/glGet.xml")
s = f.read();
f.close();

x = html.fromstring(s)
print x
text = x.text_content()

fo = open("input.txt", "w")
fo.write(text.encode('UTF-8'));
fo.close();

