  #!/usr/bin/python
  # -*- coding: utf-8 -*-

#Para limpiar el json general obtenido del repositorio

fname = raw_input("Enter a file name: ")
if ( len(fname) < 1 ) : fname = '../2015-2016/bl.json'

fh = open(fname)
stringdata=fh.read()

fh=open(fname, "w")
news=stringdata.replace("ö", "oe")
stringdata=news
news=stringdata.replace("ü", "ue")
stringdata=news
news=stringdata.replace("_x0020_", "_")
stringdata=news
news=stringdata.replace("Spieltag", "Jornada")
fh.write(news)
	
#print news



fh.close()
