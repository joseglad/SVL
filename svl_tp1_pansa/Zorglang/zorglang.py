"""
SVL 1516
Zorgland

>>> traducteur = TradZorglang()
>>> traducteur.zorglang("Hello world!")
'olleH dlrow!'
"""
import unittest

class TradZorglang():
	def zorglang(self, chaine):
		current = ''
		res = ''
		for c in chaine:
			if c == ' ':
				#on stocke un mot et un espace
				res += current + c
				#on se prépare pour le mot suivant
				current = ''
			elif c == '!':
				#on ne change pas de sens le point d'exclamation
				current = current + c
			else:
				current = c + current
		res += current
		return res

class TestTraducteur(unittest.TestCase):

	def test_la_chaine_vide_est_traduite_en_chaine_vide(self):
		traducteur = TradZorglang()
		self.assertEqual(traducteur.zorglang(""), "")

	def test_la_chaine_de_taille_1_reste_telle_quelle(self):
		traducteur = TradZorglang()
		self.assertEqual(traducteur.zorglang("a"), "a")

	def test_une_chaine_compose_de_lettres_est_retournee(self):
		traducteur = TradZorglang()
		self.assertEqual(traducteur.zorglang("pipp"), "ppip")

if __name__ == '__main__':
	unittest.main()
