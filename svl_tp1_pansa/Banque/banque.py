"""
Application bancaire : comptes
"""

class Compte():
	"""
	Représentation d'un compte bancaire.

	On peut créer un compte avec solde nul.
	>>> compte = Compte()
	>>> compte.solde
	0.0

	On peut 
	"""
	def __init__(self):
		self.solde = 0.0

	def crediter(self, montant):
		if montant <= 0:
			raise MontantIncorrectError()
		self.solde += montant

	def debiter(self, montant):
		if montant > self.solde or montant <= 0:
			raise MontantIncorrectError()
		self.solde -= montant 

class MontantIncorrectError(Exception):
	pass
