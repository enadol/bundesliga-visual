import urllib
import json
import ast


url="bl.json"
uh=urllib.urlopen(url)
data=uh.read()
#diccio=ast.literal_eval(data)
js=json.loads(data)
#print data
print type(data)
#print type(js)
print type(lst)
print js