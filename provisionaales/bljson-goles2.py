import urllib
import json

url="2015-2016/bl.json"
uh=urllib.urlopen(url)
data=uh.read()
js=json.loads(data)
i=0
ganador=None
perdedor=None
afavor=0
encontra=0
equipos=[]
totalgoles=0
sumlocal=0
sumvisitante=0

def getEquipos():
	for fecha in range(1,5):
		jornadascompletas=js['rounds'][fecha]['name']
		
		for i in range(0,9):
			equipo=js['rounds'][fecha]['matches'][i]['team1']['name']
			contrario=js['rounds'][fecha]['matches'][i]['team2']['name']
			if equipo not in equipos:
				equipos.append(equipo)
			if contrario not in equipos:
				equipos.append(contrario)
	return equipos

def printCareta(jornada, equipo, goles1, goles2):
				print jornada
				print equipo
				print "Goles a favor: "+str(goles1)
				print "Goles en Contra: "+str(goles2)+"\n"
				#print "Diferencia: "+str(diferencia1)
				print "--------------------"

def traspasar(viejo, nuevo):
	for index in range(0,len(viejo)):
		for i in nuevo:
			nuevo=viejo
	#print len(nuevo)
	return nuevo

def getGoles(equipo, goles):
	return goles

def getGolesAcumulados(goleslocal, goles):
	goleslocal=goleslocal+goles
	return goleslocal

#equipoinput=raw_input("Ingrese el equipo: ")

jornadainput=raw_input("Ingrese la jornada: ")
jornada=int(jornadainput)-1
totallocal=0
totalvisitante=0
totaldif=0


if jornada <0 or jornada >=34:
	print "No se jugó la jornada "+jornadainput+" en ese torneo. Verifique y vuelva a ingresar."
	jornada=None
else:
	clubes=getEquipos()


	#for club in clubes:
	#	lstlocal=[]
	#	lstvisitante=[]

	for fecha in range(0,jornada+1):

		jornadascompletas=js['rounds'][fecha]['name']

		for i in range(0,9):

			equipo=js['rounds'][fecha]['matches'][i]['team1']['name']
			contrario=js['rounds'][fecha]['matches'][i]['team2']['name']
			afavor=js['rounds'][fecha]['matches'][i]['score1']
			encontra=js['rounds'][fecha]['matches'][i]['score2']

			for club in clubes:
				sumlocal=0
				goleslocal=0
				golesvisitante=0
				sumvisitante=0

				if equipo==club:

					print "Local"
					#lstlocal.append(afavor)
					#lstvisitante.append(encontra)
					goleslocal=getGoles(equipo,afavor)
					sumlocal=getGolesAcumulados(sumlocal, goleslocal)
					#print goleslocal
					print "Total de goles a favor para el "+equipo+" en la jornada "+str(fecha+1)+": "+ str(sumlocal)
				#print club
				if contrario==club:
					print "Visitante"
					golesvisitante=getGoles(contrario, encontra)
						#print goleslocal
					
					sumvisitante=getGolesAcumulados(sumvisitante, golesvisitante)
					print "Total de goles a favor para el "+club+" en la jornada "+str(fecha+1)+": "+ str(sumvisitante)

			
uh.close()