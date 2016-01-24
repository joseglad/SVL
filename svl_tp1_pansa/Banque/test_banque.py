"""
Test banque
demo SVL CTD1 - M. Nebut - 1516
"""

# que teste-t-on ?
# -création d'un compte
import unittest
from banque import *
#from banque import Compte
#from banque import MontantIncorrectError

class TestCreationCompte(unittest.TestCase):
	def test_un_compte_est_cree_avec_solde_nul(self):
		compte = Compte() #indentation importante, et forcée par le langage
		#Cree un compte avec un solde nul
		self.assertEqual(compte.solde, 0.0)

class TestCrediterCompte(unittest.TestCase):
	def test_crediter_un_compte_augmente_son_solde(self):
		compte = Compte()
		compte.crediter(20.0)
		self.assertEqual(compte.solde, 20.0)
	def test_le_montant_est_positif(self):
		compte = Compte()
		self.assertRaises(MontantIncorrectError, compte.crediter, -10.0)
	
	def test_on_peut_crediter_plusieurs_fois(self):
		compte = Compte()
		compte.crediter(10.0)
		compte.crediter(30.0)
		self.assertEqual(compte.solde, 40.0)
		
	def test_le_montant_est_strictement_positif(self):
		compte = Compte()
		self.assertRaises(MontantIncorrectError, compte.crediter, 0.0)

class TestDebiterCompte(unittest.TestCase):
	def test_debiter_un_compte_diminue_son_solde(self):
		compte = Compte()
		compte.crediter(50.0)
		compte.debiter(40.0)
		self.assertEqual(compte.solde, 10.0)

	def test_le_solde_reste_positif(self):
		compte = Compte()
		#Exception, fonction, argument de la fonction
		self.assertRaises(MontantIncorrectError, compte.debiter, 10.0)

	def test_on_peut_debiter_plusieurs_fois(self):
		compte = Compte()
		compte.crediter(50.0)
		compte.debiter(20.0)
		compte.debiter(10.0)
		self.assertEqual(compte.solde, 20.0)

	def test_le_montant_est_strictement_positif(self):
		compte = Compte()
		compte.crediter(20)
		self.assertRaises(MontantIncorrectError, compte.debiter, 0.0)

		

# Si execution du test directement par python3 // On peut aussi les exécuter avec nosetests
if __name__ == '__main__':
	unittest.main()
