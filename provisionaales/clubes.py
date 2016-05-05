import urllib
import json

url="bl.json"
uh=urllib.urlopen(url)
data=uh.read()
js=json.loads(data)
equipos=[]

def getEquipos():
	for fecha in range(0,5):
		jornadascompletas=js['rounds'][fecha]['name']
		
		for i in range(0,9):
			equipo=js['rounds'][fecha]['matches'][i]['team1']['name']
			contrario=js['rounds'][fecha]['matches'][i]['team2']['name']
			if equipo not in equipos:
				equipos.append(equipo)
			if contrario not in equipos:
				equipos.append(contrario)
	return equipos

print getEquipos()
				#print contrario+"  "+str(encontra)+"  "+jornadascompletas
		