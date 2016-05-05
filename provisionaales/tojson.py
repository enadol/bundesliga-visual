import sqlite3

conn = sqlite3.connect('tabla.sqlite')
cur = conn.cursor()

print "Creating JSON output on tabla.js..."
howmany = int(raw_input("Cuantas jornadas? "))

cur.execute('''SELECT Partidos.Equipo, Partidos.Jornada, Partidos.PJ, Partidos.PG, Partidos.PE, Partidos.PP, Goles.Goles_a_favor AS GF, Goles.Goles_en_contra AS GC, Goles.Diferencia AS DIF, Puntos.Total_Puntos AS Puntos
FROM partidos JOIN Goles, Puntos WHERE Partidos.Equipo = Goles.Equipo AND Goles.Equipo=Puntos.Equipo
AND Puntos.Jornada=Partidos.Jornada AND Goles.Jornada=Puntos.Jornada AND Puntos.Jornada<='''+str(howmany)+''' 
GROUP BY Partidos.Equipo
ORDER BY Puntos DESC, DIF DESC''')

fhand = open('tabla.js','w')
nodes = list()
#maxrank = None
#minrank = None
for row in cur :
    nodes.append(row)
    
    #rank = row[2]
    #if maxrank < rank or maxrank is None : maxrank = rank
    #if minrank > rank or minrank is None : minrank = rank
    #if len(nodes) > howmany : break

#if maxrank == minrank or maxrank is None or minrank is None:
#    print "Error - please run sprank.py to compute page rank"
#    quit()

fhand.write('tablaJson = {"nodes":[\n')
count = 0
id=count+1
map = dict()
#ranks = dict()
for row in nodes :
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

print "Open force.html in a browser to view the visualization"
