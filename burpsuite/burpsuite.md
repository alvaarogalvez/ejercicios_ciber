hemos estado trabajando con burpsuite, para usarlo es necesario instalar la extension foxyproxy y instalarle los certificados, basicamente hemos usado el proxy 
![alt text](image.png)

Cuando queramos parar el trafico le damos a intercept on y recargamos pagina y nos saldra todas las llamadas es muy util para saber las llamadas http que hacemos a las paginas

![alt text](image-1.png)

Aquí nos sale todo el historial de las llamadas http que hemos hecho
Y por ultimo lo mas importante que hemos hecho es para adivinar usuarios y contraseñas


-si sabemos el usuario y la contraseña no
Le damos a sniper y seleccionamos la contaseña y cargamos en payload el diccionario
Seleccionamos solo la contaseña y metemos un diccionario para que con un usuario pruebe todas las contraseñas

![alt text](image-2.png)

![alt text](image-3.png)

Y si queremos probar contraseña y usuario a la vez

![alt text](image-4.png)

Y en cada position del payload un diccionario uno con usuario y otro con contraseñas

![alt text](image-5.png)