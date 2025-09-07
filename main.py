from Personnage import Personnage
from Arme import Arme

epee_legendaire = Arme("Epée légendaire",10)
joueur1 = Personnage("Aragorn","Guerrier",10,100,15,5,epee_legendaire)
joueur2 = Personnage("Gandalf","Magicien",1,80,5,15)

joueur1.afficher_info()
joueur2.afficher_info()

joueur1.attaquer(joueur2)
joueur2.afficher_info()