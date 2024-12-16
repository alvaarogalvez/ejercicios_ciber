pillo la solicitud y la mando a intruder
![alt text](image-4.png)

intercepto la peticion y selecciono la contraseña y le doy a add
![alt text](image-2.png)

aqui le meto en payload el diccionario de rockyou.txt para probar las contraseñas
![alt text](image-1.png)

aqui vemo como da correcto en todos pero no es verdad lo que nos tenemos que fijar en length y vemo que password es la unica diferente
![alt text](image.png)

y aqui comprobamos como me ha dejado entrar 
![alt text](image-3.png)

ahora vamos a hacer un ataque de fuerza bruta con hydra
y nos saldra todas las contraseñas para admin
hydra -l admin -P /home/alvaro/rockyou\(1\).txt "http-get-form://172.17.0.2/vulnerabilities/brute/:username=^USER^&password=^PASS^&Login=submit:Username and/or password incorrect."

![image](https://github.com/user-attachments/assets/09bf6185-e11c-4f9f-9a91-a26397e2f1da)

