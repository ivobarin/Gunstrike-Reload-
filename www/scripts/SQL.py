import sqlite3

with sqlite3.connect("bd_btf.db") as conexion:
	try:
		sentencia = ''' create  table usuarios
		(
		id integer primary key autoincrement,
		nombre text,
		score integer
		)
		'''
		conexion.execute(sentencia)
		print("Se creo la tabla usuarios")                       
	except sqlite3.OperationalError:
		print("La tabla usuarios ya existe")

	#INSERT:
	try:
		conexion.execute("insert into usuarios(nombre,score) values (?,?)", ("Adriel",110))
		conexion.execute("insert into usuarios(nombre,score) values (?,?)", ("Tito Calderon",250)) 
		conexion.execute("insert into usuarios(nombre,score) values (?,?)", ("Marko",150)) 
		conexion.execute("insert into usuarios(nombre,score) values (?,?)", ("Jorge Macri",90)) 
		conexion.execute("insert into usuarios(nombre,score) values (?,?)", ("Joey Ramone",200)) 
		conexion.commit()# Actualiza los datos realmente en la tabla
	except:
		print("Error")

	#SELECT:
	cursor=conexion.execute("SELECT * FROM usuarios")
	for fila in cursor:
		print(fila)

