#demo

#fonctionnalite pour Caisse
#- visualiser le solde de la carte
# -visualiser le nombre de tickets restau
# -visualiser la valeur d'un ticket
# -payer un repas sans ticket
# -payer un repas avec un ticket

#- visualiser le solde de la carte
#-- cas nominal : solde caisse = solde carte  => test ok
#-- pas de carte insérée : erreur => test ok

# - payer un repas sans ticket
# -- cas nominal : la carte est débitée
# -- pas assez d'argent sur la carte : erreur
# -- pas de carte insérée : erreur
# -- erreur prix repas

class Caisse:
	"""
	On eput créer une caisse.
	
	>>> caisse = Caisse()

	et on ne peut rien faire avant d'avoir rentré une carte
	>>> caisse.solde()
	Traceback (most recent call last):
	...
	restaurant.CarteManquanteError
	
	Une fois la carte insérée on peut consulter
	"""
	def __init__(self):
		self.carte = None

	def inserer_carte(self, carte):
		self.carte = carte

	def solde(self):
		if self.carte == None:
			raise CarteManquanteError()	
		return self.carte.solde()

	def payer_repas_sans_ticket(self, montant):
		self.carte.debiter(montant)
		
		
class Carte:
	"""
	On peut consulter le solde de la carte.
	>>> carte = Carte()
	>>> carte.solde()
	0.0

	>>> carte.debiter(5)
	...
	"""

class CarteManquanteError(Exception):
	pass

class SoldeInsuffisantError(Exception):
	pass
