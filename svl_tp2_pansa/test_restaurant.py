#demo

import unittest

#bibliothèque de mocks
from mockito import *
from restaurant import *

class TestCaisse(unittest.TestCase):
	def test_le_solde_caisse_est_celui_de_la_carte(self):
		caisse = Caisse()
		LE_SOLDE = 10

		#Contrainte technique on n'a pas testé la classe Carte
		#On va devoir faire une fausse carte pour les besoins du test
		#Il s'agit de Mock, utile que pour le test
		#carte = MockCarte(LE_SOLDE)
		#Quand carte reçoit un appel à solde, on retourne le solde
		carte = mock()
		when(carte).solde().thenReturn(LE_SOLDE) #pour mockito

		caisse.inserer_carte(carte)
		self.assertEqual(caisse.solde(), LE_SOLDE)

	def test_sans_carte_la_visualisation_echoue(self):
		caisse = Caisse()
		self.assertRaises(CarteManquanteError, caisse.solde)


class TestPayerUnRepasSansTicket(unittest.TestCase):
	def test_sans_ticket_la_carte_est_debitee(self):
		caisse = Caisse()
		carte = mock()
		caisse.inserer_carte(carte)

		REPAS = 7.0
		caisse.payer_repas_sans_ticket(REPAS)
		#Il faut que debiter(REPAS) soit appelée 
		#pour simuler que la carte est débitée
		#verify vérifie que l'appel a debiter a été fait
		verify(carte).debiter(REPAS)

	def test_sans_ticket_pas_suffisamment_d_argent_le_paiement_echoue(self):
		caisse = Caisse()
		carte = mock()
		caisse.inserer_carte(carte)
		
		REPAS = 7.0
		when(carte).debiter(REPAS).thenRaise(SoldeInsuffisantError(), caisse.payer_repas_sans_ticket, REPAS)
		self.assertRaises(SoldeInsuffisantError, caisse.payer_repas_sans_ticket, REPAS)
	"""
	def test_sans_carte_la_visualisation_echoue(self):
		caisse = Caisse()
		self.assertRaises(CarteManquanteError, caisse.solde)
	"""

class MockCarte():
	"""
	Pour mock manuel
	"""
	def __init__(self, montant):
		self.montant = montant

	def solde(self):
		return self.montant


if __name__ == '__main__':
	unittest.main()
		
