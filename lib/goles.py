﻿import urllib
import json
import sqlite3

url="2015-2016/bl.json"
uh=urllib.urlopen(url)
data=uh.read()
js=json.loads(data)
i=0

afavor=0
encontra=0
equipos=[]


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

	return nuevo

def getGoles(equipo, goles):
	return goles

def getGolesAcumulados(goleslocal, goles):
	goleslocal=goleslocal+goles
	return goleslocal

jornadainput=raw_input("Ingrese la jornada: ")
jornada=int(jornadainput)-1

if jornada <0 or jornada >=34:
	print "No se jugó la jornada "+jornadainput+" en ese torneo. Verifique y vuelva a ingresar."
	jornada=None
else:
	clubes=getEquipos()



	for club in clubes:
		subtotaluno=0
		golesuno=0
		golesdos=0
		subtotaldos=0
		golesa=0
		golesb=0
		subtotala=0
		subtotalb=0
		diferencia=0
		for fecha in range(0,jornada+1):

			jornadascompletas=js['rounds'][fecha]['name']
			conn = sqlite3.connect('tabla.sqlite')
			cur = conn.cursor()
			conn.text_factory = str
			start = 0

			cur.execute('''CREATE TABLE IF NOT EXISTS Goles 
			(Equipo TEXT, Jornada INTEGER, 
			Goles_a_favor INTEGER, Goles_en_contra INTEGER, Diferencia INTEGER)''')

			for i in range(0,9):



				equipo=js['rounds'][fecha]['matches'][i]['team1']['name']
				contrario=js['rounds'][fecha]['matches'][i]['team2']['name']
				afavor=js['rounds'][fecha]['matches'][i]['score1']
				encontra=js['rounds'][fecha]['matches'][i]['score2']

			

				if equipo==club:

					
					golesuno=getGoles(equipo,afavor)
					golesa=getGoles(contrario, encontra)

					subtotaluno=getGolesAcumulados(subtotaluno, golesuno)
					subtotala=getGolesAcumulados(subtotala, golesa)
					

				if contrario==club:
					
					golesdos=getGoles(contrario, encontra)
					golesb=getGoles(equipo, afavor)

					subtotaldos=getGolesAcumulados(subtotaldos, golesdos)
					subtotalb=getGolesAcumulados(subtotalb, golesb)
				sumtotalfavor=subtotaluno+subtotaldos
				sumtotalcontra=subtotala+subtotalb
				diferencia=sumtotalfavor-sumtotalcontra
			
			start +=1
			print "Goles acumulados a favor para el "+club+" en la jornada "+str(fecha+1)+": "+ str(sumtotalfavor)
			print "Goles acumulados en contra para el "+club+" en la jornada "+str(fecha+1)+": "+ str(sumtotalcontra)
			print "Diferencia acumulada de goles para el "+club+" en la jornada "+str(fecha+1)+": "+ str(diferencia)+"\n"
			cur.execute('''INSERT OR IGNORE INTO Goles (Equipo, Jornada, Goles_a_favor, Goles_en_contra, Diferencia)  VALUES (?, ?, ?, ?, ? )''', (club, fecha+1, sumtotalfavor, sumtotalcontra, diferencia))
		
			#cur.execute('SELECT max(id) FROM Goles')
			#try:
			#	row = cur.fetchone()
    		#	if row[0] != None: 
        	#		start = row[0]
			#except:
   			#	 start = 0
   			#	 row = None

#print start

			

			conn.commit()
	

			
uh.close()
cur.close()