import urllib
import json


uh=urllib.urlopen(url)
data=uh.read()
js=json.loads(data)
i=0
ganador=None
perdedor=None


jornadainput=raw_input("Ingrese la jornada: ")
jornada=int(jornadainput)-1

if jornada <0 or jornada >=34:
	print "No se jugó la jornada "+jornadainput+" en ese torneo. Verifique y vuelva a ingresar."
	jornada=None
else:
	for i in range(1,9):
		jornadascompletas=js['rounds'][0]['name']
		equipo=js['rounds'][jornada]['matches'][i]['team1']['name']
		contrario=js['rounds'][jornada]['matches'][i]['team2']['name']
		afavor=js['rounds'][jornada]['matches'][i]['score1']
		partido=js['rounds'][jornada]['matches'][i]
		encontra=js['rounds'][jornada]['matches'][i]['score2']
		i+=1
	
		if afavor > encontra:
			puntos=3
			ganador=equipo
			perdedor=contrario
		elif afavor==encontra:
			puntos=1
			ganador="Empate"
			perdedor=ganador
		else:
			puntos=0
			ganador=contrario
			perdedor=equipo

		print equipo +" "+str(afavor)+' - '+str(encontra)+" "+contrario+" ** Ganador: "+ganador

	
uh.close()
