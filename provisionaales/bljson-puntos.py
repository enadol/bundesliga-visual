import urllib
import json

url="2015-2016/bl.json"
uh=urllib.urlopen(url)
data=uh.read()
js=json.loads(data)
i=0
ganador=None
perdedor=None
puntoslocal=0
puntosvisitante=0
sumavisitante=0
puntos=0
sumalocal=0

def getPuntos(equipo, afavor, encontra):
	puntos=0
	
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
	
	return puntos

def getPuntosAcumulados(puntoslocal, puntos):
	puntoslocal=puntoslocal+puntos
	return puntoslocal
	


jornadainput=raw_input("Ingrese la jornada: ")
jornada=int(jornadainput)-1

equipoinput=raw_input("Ingrese el equipo: ")

if jornada <0 or jornada >=34:
	print "No se jugó la jornada "+jornadainput+" en ese torneo. Verifique y vuelva a ingresar."
	jornada=None
else:
	for fecha in range(0,jornada+1):
		jornadascompletas=js['rounds'][fecha]['name']
				
		for i in range(0,9):
			equipo=js['rounds'][fecha]['matches'][i]['team1']['name']
			afavor=js['rounds'][fecha]['matches'][i]['score1']
			contrario=js['rounds'][fecha]['matches'][i]['team2']['name']
			encontra=js['rounds'][fecha]['matches'][i]['score2']

			if equipo>0 and equipo==equipoinput:
				puntoslocal=getPuntos(equipo, afavor, encontra)
				
				sumalocal=getPuntosAcumulados(sumalocal, puntoslocal)
		

			if equipo>0 and contrario==equipoinput:
				puntosvisitante=getPuntos(contrario, encontra, afavor)	
		
				sumavisitante=getPuntosAcumulados(sumavisitante, puntosvisitante)
		sumapuntos=sumalocal+sumavisitante
	print "El equipo "+equipoinput+" sumaba "+str(sumalocal)+" como local a la "+jornadascompletas
	print "El equipo "+equipoinput+" sumaba "+str(sumavisitante)+" como visitante a la "+jornadascompletas	
	print "El equipo "+equipoinput+" sumaba "+str(sumapuntos)+" puntos en total a la "+jornadascompletas
				
	
uh.close()
