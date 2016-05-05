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
fecha=0

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

def traspasar(viejo, nuevo):
	for index in range(0,len(viejo)):
		for i in nuevo:
			nuevo=viejo
	#print len(nuevo)
	return nuevo



jornadainput=raw_input("Ingrese la jornada: ")
jornada=int(jornadainput)-1

#equipoinput=raw_input("Ingrese el equipo: ")

if jornada <0 or jornada >=34:
	print "No se jugó la jornada "+jornadainput+" en ese torneo. Verifique y vuelva a ingresar."
	jornada=None
else:
	clubes=getEquipos()
	lstlocal=[]
	lstvisitante=[]
	lstdiferencia=[]
	
	for fecha in range(0,jornada+1):
		jornadascompletas=js['rounds'][fecha]['name']
		sumagoles=0
		sumacontra=0
		totalafavor=0
		totalcontra=0
				
		

		for i in range(0,9):
			
			equipo=js['rounds'][fecha]['matches'][i]['team1']['name']
			contrario=js['rounds'][fecha]['matches'][i]['team2']['name']
			afavor=js['rounds'][fecha]['matches'][i]['score1']
			encontra=js['rounds'][fecha]['matches'][i]['score2']
			favorlocal=0
			favorvisitante=0
			contralocal=0
			contravisitante=0
			diferencia1=afavor-encontra
			diferencia2=encontra-afavor


			for club in clubes:
				lstnueva=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
			
			lstlocal.append(afavor)
			lstvisitante.append(encontra)
			lstlocal.append(encontra)
			lstvisitante.append(afavor)
			lstdiferencia.append(diferencia1)
			lstdiferencia.append(diferencia2)

			print jornadascompletas
			print equipo
			print "Goles a favor: "+str(afavor)
			print "Goles en contra: "+str(encontra)
			print "Diferencia: "+str(diferencia1)+"\n"
			
			print contrario
			print "Goles a favor: "+ str(encontra)
			print "Goles en contra: "+str(afavor)
			print "Diferencia: "+str(diferencia2)+"\n"
			
			print "----------------------------"
totallocal=traspasar(lstlocal, lstnueva)
totalvisitante=traspasar(lstvisitante, lstnueva)
totaldiferencia=traspasar(lstdiferencia, lstnueva)
#print totallocal
#print totalvisitante
#print lstdiferencia
	
			
uh.close()
#print getEquipos()
