import urllib
import json
import sqlite3

url="2015-2016/bl.json"
uh=urllib.urlopen(url)
data=uh.read()
js=json.loads(data)

equipos=[]
clubes=[]
lstlocal=[]
lstvisitante=[]
lstdiferencia=[]
lstnueva=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]



class Tabla(object):
	

	#jornadainput=raw_input("Ingrese la jornada: ")
	#temporadainput=raw_input("Ingrese la temporada: ")
	#jornada=int(jornadainput)-1

	
		
	countganados=0
	countempatados=0
	countperdidos=0
	countpartidos=0

	def __init__(self, temporada, jornada):
		self.temporada=temporada
		self.jornada=jornada
		#self.equipos=equipos
		#equipos=getEquipos()
		##equipoinput=raw_input("Ingrese el equipo: ")
		
	
		
	def traspasar(viejo, nuevo):
		for index in range(0,len(viejo)):
			for i in nuevo:
				nuevo=viejo
			#print len(nuevo)
			return nuevo

	def getPuntos(equipo, afavor, encontra):
			clubes=equipos
			puntos=0
			countganados=0
			countperdidos=0
			countpartidos=0
			countempatados=0

			if afavor > encontra:
				puntos=3
				ganador=equipo
				perdedor=contrario
				countganados+=1
				countpartidos+=1
			elif afavor==encontra:
				puntos=1
				ganador="Empate"
				perdedor=ganador
				countempatados+=1
				countpartidos+=1
			else:
				puntos=0
				ganador=contrario
				perdedor=equipo
				countperdidos+=1
				countpartidos+=1

			return puntos
			return countpartidos

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

	def getResultadosCompletos(jornada):
		

		if jornada <0 or jornada >=34:
			print "No se jugo la jornada "+jornadainput+" en ese torneo. Verifique y vuelva a ingresar."
			jornada=None
		else:
			clubes=equipos

			for fecha in range(0,jornada):
				jornadascompletas=js['rounds'][fecha]['name']

				for i in range(0,9):
			
					equipo=js['rounds'][fecha]['matches'][i]['team1']['name']
					contrario=js['rounds'][fecha]['matches'][i]['team2']['name']
					afavor=js['rounds'][fecha]['matches'][i]['score1']
					encontra=js['rounds'][fecha]['matches'][i]['score2']
					#afavor=0
					#encontra=0
					#print afavor
					#print encontra

					sumagoles=0
					sumacontra=0
					totalafavor=0
					totalcontra=0

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
					print "Goles en Contra: "+str(encontra)
					print "Diferencia: "+str(diferencia1)+"\n"
			
					print contrario
					print "Goles a favor: "+ str(encontra)
					print "Goles en contra: "+str(afavor)
					print "Diferencia: "+str(diferencia2)+"\n"
		
					print "----------------------------"

			#print lstlocal
			#print lstvisitante
			#print lstdiferencia	
	totallocal=traspasar(lstlocal, lstnueva)
	totalvisitante=traspasar(lstvisitante, lstnueva)
	totaldiferencia=traspasar(lstdiferencia, lstnueva)

	#print totallocal
	#print totalvisitante
	#print totaldiferencia

	#uh.close()

	def getPuntosAcumulados(puntoslocal, puntos):
			puntoslocal=puntoslocal+puntos
			return puntoslocal


#TO-DO VERIFICAR OUTPUT CON METODOS	
#TO-DO Verificar por que no llega el getEquipos() a clubes=equipos
	def getTablaPuntos(jornada):
		clubes=getEquipos()
		print clubes	


		if jornada <0 or jornada >=34:
			print "No se jugo la jornada "+jornadainput+" en ese torneo. Verifique y vuelva a ingresar."
			jornada=None
		else:

			for fecha in range(0,jornada):
				jornadascompletas=js['rounds'][fecha]['name']
				print jornadascompletas

				for i in range(0,9):
					equipo=js['rounds'][fecha]['matches'][i]['team1']['name']
					afavor=js['rounds'][fecha]['matches'][i]['score1']
					contrario=js['rounds'][fecha]['matches'][i]['team2']['name']
					encontra=js['rounds'][fecha]['matches'][i]['score2']
						
					sumalocal=0
					sumavisitante=0

					#print jornadascompletas
					#print equipo
					#print contrario
					#print afavor
					#print encontra

			for club in clubes:
				print club
						
				if equipo>0 and equipo==equipo:
					puntoslocal=getPuntos(equipo, afavor, encontra)
				
					sumalocal=getPuntosAcumulados(sumalocal, puntoslocal)
		

				if equipo>0 and equipo==contrario:
					puntosvisitante=getPuntos(equipo, encontra, afavor)	
		
					sumavisitante=getPuntosAcumulados(sumavisitante, puntosvisitante)
			#print "El equipo "+equipo+" sumaba "+str(sumalocal)+" como local a la "+jornadascompletas
		#sumapuntos=sumalocal+sumavisitante
					
			#print "El equipo "+equipo+" sumaba "+str(sumavisitante)+" como visitante a la "+jornadascompletas	
			#print "El equipo "+equipo+" sumaba "+str(sumapuntos)+" puntos en total a la "+jornadascompletas
			
	
	uh.close()







	

#prueba=Tabla("2014-2015", 5)
#getEquipos()
#getResultadosCompletos(5)
#getTablaPuntos(30)

