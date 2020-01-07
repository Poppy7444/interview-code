# python脚本
import re

regex = r"https?:\/\/(?P<site>[1-9a-z.]*)"
sites = set()

with open("demo.txt","r") as f:
    line = f.readline()
    while line:
        sites.add(re.search(regex,line).group(1))
        line = f.readline()

print('demo.txt中共包含{0}个不同的网站'.format(str(len(sites))))