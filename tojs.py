import sqlite3

conn = sqlite3.connect('../tabla.sqlite')
cur = conn.cursor()

print "Creating Javascript output on tabla.js..."
howmany = int(raw_input("Cuantas jornadas? "))

cur.execute('''SELECT Partidos.Equipo, Partidos.Jornada, Partidos.PJ, Partidos.PG, Partidos.PE, Partidos.PP, Goles.Goles_a_favor AS GF, Goles.Goles_en_contra AS GC, Goles.Diferencia AS DIF, Puntos.Total_Puntos AS Puntos
FROM Partidos JOIN Goles, Puntos WHERE Partidos.Equipo = Goles.Equipo AND Goles.Equipo=Puntos.Equipo
AND Puntos.Jornada=Partidos.Jornada AND Goles.Jornada=Puntos.Jornada AND Puntos.Jornada<='''+str(howmany)+''' 
GROUP BY Partidos.Equipo
ORDER BY Puntos DESC, DIF DESC''')

fhand = open('../js/tablavoll.js','w')
nodes = list()

for row in cur :
    nodes.append(row)
   

fhand.write('tablaJson = {"nodes":[\n')
count = 0
id=count+1
map = dict()
#ranks = dict()
for row in nodes :
    if count > 0 : fhand.write(',\n')
    fhand.write('{'+'"id":'+str(id)+',"equipo":"'+str(row[0])+'","jornada":'+str(row[1])+',"jugados":'+str(row[2])+',"ganados":'+str(row[3])
    +',"empatados":'+str(row[4])+',"perdidos":'+str(row[5])+',"gf":'+str(row[6])+',"gc":'+str(row[7])+',"dif":'+str(row[8])
    +',"puntos":'+str(row[9])+'}')

    count=count+1
    id = id+1
fhand.write(']};')
fhand.close()

#tablalocal
fhand = open('../js/tablalocal.js','w')
nodes = list()

cur.execute('''SELECT Partidos.Equipo, Partidos.Jornada, Partidos.PJ_Local, Partidos.PG_Local, Partidos.PE_Local, Partidos.PP_Local, GolesLocal.Goles_a_favor AS GF, GolesLocal.Goles_en_contra AS GC, GolesLocal.Diferencia AS DIF, Puntos.Puntos_Local AS Puntos
FROM partidos JOIN GolesLocal, Puntos WHERE Partidos.Equipo = GolesLocal.Equipo AND GolesLocal.Equipo=Puntos.Equipo
AND Puntos.Jornada=Partidos.Jornada AND GolesLocal.Jornada=Puntos.Jornada AND Puntos.Jornada<='''+str(howmany)+''' 
GROUP BY Partidos.Equipo
ORDER BY Puntos DESC, DIF DESC''')

#fhand = open('tablavoll.js','w')
nodeslocal = list()
for row in cur :
    nodeslocal.append(row)
    
    #rank = row[2]
    #if maxrank < rank or maxrank is None : maxrank = rank
    #if minrank > rank or minrank is None : minrank = rank
    #if len(nodes) > howmany : break

#if maxrank == minrank or maxrank is None or minrank is None:
#    print "Error - please run sprank.py to compute page rank"
#    quit()

fhand.write('\n\ntablalocal = {"nodes":[\n')
count = 0
id=count+1
map = dict()
#ranks = dict()
for row in nodeslocal :
    if count > 0 : fhand.write(',\n')
    # print row
 #   rank = row[2]
 #   rank = 19 * ( (rank - minrank) / (maxrank - minrank) ) 
    fhand.write('{'+'"id":'+str(id)+',"equipo":"'+str(row[0])+'","jornada":'+str(row[1])+',"jugados":'+str(row[2])+',"ganados":'+str(row[3])
    +',"empatados":'+str(row[4])+',"perdidos":'+str(row[5])+',"gf":'+str(row[6])+',"gc":'+str(row[7])+',"dif":'+str(row[8])
    +',"puntos":'+str(row[9])+'}')
    #fhand.write(' "id":'+str(row[3])+', "url":"'+row[4]+'"}')
    #map[row[3]] = count
    #ranks[row[3]] = rank
    count=count+1
    id = id+1
fhand.write(']};')

fhand.close()

#tablavisitante
fhand = open('../js/tablavisitante.js','w')
nodes = list()

cur.execute('''SELECT Partidos.Equipo, Partidos.Jornada, Partidos.PJ_Visitante, Partidos.PG__Visitante, Partidos.PE_Visitante, Partidos.PP_Visitante, GolesVisitante.Goles_a_favor AS GF, GolesVisitante.Goles_en_contra AS GC, GolesVisitante.Diferencia AS DIF, Puntos.Puntos_Visitante AS Puntos
FROM partidos JOIN GolesVisitante, Puntos WHERE Partidos.Equipo = GolesVisitante.Equipo AND GolesVisitante.Equipo=Puntos.Equipo
AND Puntos.Jornada=Partidos.Jornada AND GolesVisitante.Jornada=Puntos.Jornada AND Puntos.Jornada<='''+str(howmany)+''' 
GROUP BY Partidos.Equipo
ORDER BY Puntos DESC, DIF DESC''')

nodesvisitante = list()

for row in cur :
    nodesvisitante.append(row)
    
fhand.write('\n\ntablavisitante = {"nodes":[\n')
count = 0
id=count+1
map = dict()
#ranks = dict()
for row in nodesvisitante :
    if count > 0 : fhand.write(',\n')
    # print row
 #   rank = row[2]
 #   rank = 19 * ( (rank - minrank) / (maxrank - minrank) ) 
    fhand.write('{'+'"id":'+str(id)+',"equipo":"'+str(row[0])+'","jornada":'+str(row[1])+',"jugados":'+str(row[2])+',"ganados":'+str(row[3])
    +',"empatados":'+str(row[4])+',"perdidos":'+str(row[5])+',"gf":'+str(row[6])+',"gc":'+str(row[7])+',"dif":'+str(row[8])
    +',"puntos":'+str(row[9])+'}')
    #fhand.write(' "id":'+str(row[3])+', "url":"'+row[4]+'"}')
    #map[row[3]] = count
    #ranks[row[3]] = rank
    count=count+1
    id = id+1
fhand.write(']};')

fhand.close()
cur.close()

print "NO OLVIDAR PARA BLVISUAL.HTML CAMBIAR EQUIPO POR NAME Y PUNTOS POR SIZE"
