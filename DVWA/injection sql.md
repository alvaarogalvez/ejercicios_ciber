# SQL INJECTION
-lo primero que tenemos que hacer es comprobar si al inyectar una comilla simple ' nos devuelve un error, una vez que haya devuelto un error, ya sabemos que interpreta la comilla '

-1' OR '1'='1 con esto engañamos a la base de datos y lo toma como verdadera la consulta y nos devuelve los valores de la tabla users

-1' UNION SELECT null, table_name FROM information_schema.tables WHERE table_schema=database()-- con esto nos muestra todas las tablas de la base de datos porque el campo "User ID" es vulnerable a inyección SQL, lo que significa que la entrada del usuario no está debidamente filtrada o validada. Al insertar la cadena se modifica la consulta original, permitiendo combinar su resultado con otra consulta que lista todas las tablas de la base de datos.

El uso del UNION permite recuperar información adicional, mientras que information_schema proporciona los metadatos de la base de datos.





