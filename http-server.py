#coding:utf-8
import http.server
import time
import sys
import os

# La commande habituelle pour le 'cls' dans le terminal avant l'exécution du script en lui même.
def clsa():
	linux = 'clear'
	windows = 'cls'
	os.system([linux, windows][os.name == 'nt'])
clsa()

port = 80 # Port habituel utilisé pour ce genre de script
address = ("", port) # Pour le localhost pas besoin de mettre un nom de dommaine ou autre, pour lui dire que c'est en local, on met : ""

server = http.server.HTTPServer # Création du server HTTP.

handler = http.server.CGIHTTPRequestHandler # Le handler  
handler.cgi_directories = ["/"] # Pour donner le répertoire pour le texte qui sera ensuite afficher sur le localhost.
# Pour le répertoire, si votre script en Python qui permet d'écrire votre code, est dans le même endroit que ce script il faudra juste mettre le "/"

httpd = server(address, handler)

# Message dans la console
print("> HTTP Server")
print("> Démarrage en cours..")
time.sleep(2)
print("> Serveur HTTP démarré sur le PORT {}".format(port))

httpd.serve_forever() # Pour démarré et éteindre le serveur quand on veut
