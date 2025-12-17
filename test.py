"""
Tests unitaires complets pour MathCraft
Exécuter avec: python -m unittest App.tests_complets -v
"""
import unittest
import math
import sys
import os

# Ajouter le chemin pour importer les modules
sys.path.append(os.path.dirname(__file__))

from App.modules import (
    # Arithmétique
    factorec, factoiter, nb_premier, pgcdrec, ppcm, nbr_parfait, nbr_distinct,
    puissance, puissanceRapide, catalan, combinaison, fibo, fibo2,
    
    # Trigonométrie
    cosinus, sinus,
    
    # Tableaux
    minimumTab, maximumTab, inverseTab, sommetab, moyennetab, tribulles,
    
    # Polynômes
    polynome1, polynome2, polynome3,
    
    # Chaînes
    compterVoyelles, compterlettre, compter_occurrences, palindrome,
    
    # Intégration
    intRectangleRetro, intRectanglePro, intRectangleCentre,
    intTrapezeS, intTrapezeC, intSimpsonS, intSimpsonC,
    
    # Équations
    racineDichotomie, racineNewton
)

from App.conversion import (
    convertir_longueur, convertir_temperature, convertir_masse_et_poids,
    convertir_vitesse, convertir_angles
)

class TestArithmetique(unittest.TestCase):
    """Tests pour les fonctions arithmétiques"""
    
    def test_factorec(self):
        self.assertEqual(factorec(0), 1)
        self.assertEqual(factorec(1), 1)
        self.assertEqual(factorec(5), 120)
        self.assertEqual(factorec(7), 5040)
    
    def test_factoiter(self):
        self.assertEqual(factoiter(0), 1)
        self.assertEqual(factoiter(1), 1)
        self.assertEqual(factoiter(5), 120)
        self.assertEqual(factoiter(7), 5040)
    
    def test_nb_premier(self):
        self.assertEqual(nb_premier(2), "✅ Ce nombre est Premier")
        self.assertEqual(nb_premier(17), "✅ Ce nombre est Premier")
        self.assertEqual(nb_premier(4), "❌ Ce nombre est Non premier")
        self.assertEqual(nb_premier(1), "❌ Ce nombre est Non premier")
    
    def test_pgcdrec(self):
        self.assertEqual(pgcdrec(48, 18), 6)
        self.assertEqual(pgcdrec(17, 13), 1)
        self.assertEqual(pgcdrec(0, 5), 5)
        self.assertEqual(pgcdrec(100, 100), 100)
    
    def test_ppcm(self):
        self.assertEqual(ppcm(12, 18), 36.0)
        self.assertEqual(ppcm(7, 3), 21.0)
        self.assertEqual(ppcm(4, 6), 12.0)
    
    def test_nbr_parfait(self):
        self.assertEqual(nbr_parfait(6), "✅ Ce nombre est parfait")
        self.assertEqual(nbr_parfait(28), "✅ Ce nombre est parfait")
        self.assertEqual(nbr_parfait(12), "❌ Ce nombre n'est pas parfait")
        self.assertEqual(nbr_parfait(496), "✅ Ce nombre est parfait")
    
    def test_nbr_distinct(self):
        self.assertEqual(nbr_distinct(1234), "❌ Ce nombre est distinct")
        self.assertEqual(nbr_distinct(1123), "✅ Ce nombre n'est pas distinct")
        self.assertEqual(nbr_distinct(7), "❌ Ce nombre est distinct")
    
    def test_puissance(self):
        self.assertEqual(puissance(2, 3), 8)
        self.assertEqual(puissance(5, 0), 1)
        self.assertEqual(puissance(2, -1), 0.5)
    
    def test_puissanceRapide(self):
        self.assertEqual(puissanceRapide(2, 3), 8)
        self.assertEqual(puissanceRapide(3, 4), 81)
    
    def test_catalan(self):
        self.assertEqual(catalan(0), 1)
        self.assertEqual(catalan(1), 1)
        self.assertEqual(catalan(3), 5)
        self.assertEqual(catalan(4), 14)
    
    def test_combinaison(self):
        self.assertEqual(combinaison(2, 5), 10.0)
        self.assertEqual(combinaison(3, 7), 35.0)
        self.assertIn("impossible", combinaison(6, 5))
    
    def test_fibonacci(self):
        self.assertEqual(fibo(0), 0)
        self.assertEqual(fibo(1), 1)
        self.assertEqual(fibo(6), 8)
        
        self.assertEqual(fibo2(0), 0)
        self.assertEqual(fibo2(1), 1)
        self.assertEqual(fibo2(6), 8)

class TestTrigonometric(unittest.TestCase):
    """Tests pour les fonctions trigonométriques"""
    
    def test_cosinus(self):
        # Test avec une précision de 0.0001
        self.assertAlmostEqual(cosinus(0, 0.0001), 1.0, places=3)
        self.assertAlmostEqual(cosinus(math.pi/3, 0.0001), 0.5, places=3)
    
    def test_sinus(self):
        self.assertAlmostEqual(sinus(0, 0.0001), 0.0, places=3)
        self.assertAlmostEqual(sinus(math.pi/2, 0.0001), 1.0, places=3)

class TestTableaux(unittest.TestCase):
    """Tests pour les opérations sur les tableaux"""
    
    def setUp(self):
        self.tab1 = [3, 1, 4, 1, 5, 9, 2]
        self.tab2 = [-5, 10, 2, 8, -1]
        self.tab3 = [5]
    
    def test_minimumTab(self):
        self.assertEqual(minimumTab(self.tab1), 1)
        self.assertEqual(minimumTab(self.tab2), -5)
        self.assertEqual(minimumTab(self.tab3), 5)
    
    def test_maximumTab(self):
        self.assertEqual(maximumTab(self.tab1), 9)
        self.assertEqual(maximumTab(self.tab2), 10)
        self.assertEqual(maximumTab(self.tab3), 5)
    
    def test_inverseTab(self):
        self.assertEqual(inverseTab(self.tab1), [2, 9, 5, 1, 4, 1, 3])
        self.assertEqual(inverseTab([1, 2, 3]), [3, 2, 1])
    
    def test_sommetab(self):
        self.assertEqual(sommetab(self.tab1), 25)
        self.assertEqual(sommetab([1, 2, 3]), 6)
    
    def test_moyennetab(self):
        self.assertAlmostEqual(moyennetab([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(moyennetab([10, 20]), 15.0)
    
    def test_tribulles(self):
        self.assertEqual(tribulles([3, 1, 4, 2]), [1, 2, 3, 4])
        self.assertEqual(tribulles([5, -1, 0, 3]), [-1, 0, 3, 5])

class TestPolynomes(unittest.TestCase):
    """Tests pour la résolution d'équations polynomiales"""
    
    def test_polynome1(self):
        # 2x + 4 = 0 → x = -2
        result = polynome1(2, 4)
        self.assertIn("x = -2.00", result)
        
        # 0x + 5 = 0 → pas de solution
        result = polynome1(0, 5)
        self.assertIn("ne peut pas être nul", result)
    
    def test_polynome2(self):
        # x² - 5x + 6 = 0 → x=2, x=3
        result = polynome2(1, -5, 6)
        self.assertIn("x₁ = 2.00", result)
        self.assertIn("x₂ = 3.00", result)
        
        # x² + 1 = 0 → solutions complexes
        result = polynome2(1, 0, 1)
        self.assertIn("complexes", result)
        
        # x² - 2x + 1 = 0 → solution double
        result = polynome2(1, -2, 1)
        self.assertIn("solution double", result)
    
    def test_polynome3(self):
        # x³ - 6x² + 11x - 6 = 0 → x=1,2,3
        result = polynome3(1, -6, 11, -6)
        self.assertIn("Trois solutions réelles distinctes", result)
        self.assertIn("x₁ = 1.00", result)
        self.assertIn("x₂ = 2.00", result)
        self.assertIn("x₃ = 3.00", result)

class TestChainesCaracteres(unittest.TestCase):
    """Tests pour les opérations sur les chaînes"""
    
    def test_compterVoyelles(self):
        self.assertEqual(compterVoyelles("Bonjour"), 3)
        self.assertEqual(compterVoyelles("Python"), 2)
        self.assertEqual(compterVoyelles("AEIOUY"), 6)
        self.assertEqual(compterVoyelles(""), 0
        )
    
    def test_compterlettre(self):
        self.assertEqual(compterlettre("bonjour", "o"), "Il y'a 2 fois o")
        self.assertEqual(compterlettre("hello", "l"), "Il y'a 2 fois l")
        self.assertEqual(compterlettre("test", "z"), "Il y'a 0 fois z")
    
    def test_compter_occurrences(self):
        self.assertEqual(compter_occurrences("bonjour bonjour", "bonjour"), 
                         "Il y'a 2 fois bonjour")
        self.assertEqual(compter_occurrences("hello world", "hello"), 
                         "Il y'a 1 fois hello")
    
    def test_palindrome(self):
        self.assertEqual(palindrome("radar"), "✅ C'est un palindrome")
        self.assertEqual(palindrome("bonjour"), "❌ Réessayer, ce n'est pas un palindrome")
        self.assertEqual(palindrome("A man a plan a canal Panama"), 
                         "✅ C'est un palindrome")

class TestIntegrationNumerique(unittest.TestCase):
    """Tests pour les méthodes d'intégration numérique"""
    
    def test_intRectangleRetro(self):
        def f(x): return x  # ∫x dx = x²/2
        result, iterations = intRectangleRetro(f, 0, 2, 1000)
        self.assertAlmostEqual(result, 2.0, places=1)
    
    def test_intRectanglePro(self):
        def f(x): return 1  # ∫1 dx = x
        result, iterations = intRectanglePro(f, 0, 5, 1000)
        self.assertAlmostEqual(result, 5.0, places=1)
    
    def test_intRectangleCentre(self):
        def f(x): return x  # ∫x dx = x²/2
        result, iterations = intRectangleCentre(f, 0, 2, 1000)
        self.assertAlmostEqual(result, 2.0, places=1)
    
    def test_intTrapezeSimple(self):
        def f(x): return 2*x  # ∫2x dx = x²
        result, iterations = intTrapezeS(f, 0, 3, 1000)
        self.assertAlmostEqual(result, 9.0, places=1)
    
    def test_intSimpsonSimple(self):
        def f(x): return x**2  # ∫x² dx = x³/3
        result, iterations = intSimpsonS(f, 0, 3, 1000)
        self.assertAlmostEqual(result, 9.0, places=1)

class TestEquationsNonLineaires(unittest.TestCase):
    """Tests pour la résolution d'équations non linéaires"""
    
    def test_racineDichotomie(self):
        def f(x): return x**2 - 4  # racine à x=2
        racine, nb_iter, details = racineDichotomie(0, 3, 0.0001, f)
        self.assertAlmostEqual(racine, 2.0, places=3)
        self.assertGreater(nb_iter, 0)
    
    def test_racineNewton(self):
        def f(x): return x**2 - 4
        def df(x): return 2*x
        racine, nb_iter, details = racineNewton(f, df, 3, 0.0001)
        self.assertAlmostEqual(racine, 2.0, places=3)
        self.assertGreater(nb_iter, 0)

class TestConversions(unittest.TestCase):
    """Tests pour les conversions d'unités"""
    
    def test_convertir_longueur(self):
        # 1 km = 1000 m
        result = convertir_longueur(1, "Kilomètre", "Mètre")
        self.assertIn("✅1000.0", result)
        
        # 100 cm = 1 m
        result = convertir_longueur(100, "Centimètre", "Mètre")
        self.assertIn("✅1.0", result)
        
        # Test d'erreur
        result = convertir_longueur("abc", "Kilomètre", "Mètre")
        self.assertIn("❌Erreur", result)
    
    def test_convertir_temperature(self):
        # 0°C = 32°F
        result = convertir_temperature(0, "Dégrés (°C)", "Fahrenheit (°F)")
        self.assertIn("✅32.0", result)
        
        # 100°C = 212°F
        result = convertir_temperature(100, "Dégrés (°C)", "Fahrenheit (°F)")
        self.assertIn("✅212.0", result)
        
        # 0°C = 273.15K
        result = convertir_temperature(0, "Dégrés (°C)", "Kelvin (°K)")
        self.assertIn("✅273.15", result)
    
    def test_convertir_masse_et_poids(self):
        # 1 kg = 1000 g
        result = convertir_masse_et_poids(1, "Kilogramme", "Gramme")
        self.assertIn("✅1000.0", result)
        
        # 1000 g = 1 kg
        result = convertir_masse_et_poids(1000, "Gramme", "Kilogramme")
        self.assertIn("✅1.0", result)
    
    def test_convertir_vitesse(self):
        # 1 m/s = 3.6 km/h
        result = convertir_vitesse(1, "Mètre par seconde", "Kilomètre par heure")
        self.assertTrue(result.startswith("✅"))
        self.assertAlmostEqual(float(result[1:]), 3.6, places=3)
    
    def test_convertir_angles(self):
        # 180° = π radians
        result = convertir_angles(180, "Degré", "Radian")
        self.assertTrue(result.startswith("✅"))
        self.assertAlmostEqual(float(result[1:]), math.pi, places=3)
        
        # π radians = 180°
        result = convertir_angles(math.pi, "Radian", "Degré")
        self.assertTrue(result.startswith("✅"))
        self.assertAlmostEqual(float(result[1:]), 180.0, places=3)

class TestFonctionsComplexes(unittest.TestCase):
    """Tests pour des cas complexes et limites"""
    
    def test_grandes_valeurs(self):
        # Test avec de grandes valeurs
        self.assertEqual(pgcdrec(123456, 123456), 123456)
        self.assertEqual(ppcm(100, 100), 100.0)
    
    def test_valeurs_negatives(self):
        # Test avec valeurs négatives
        self.assertEqual(pgcdrec(-48, 18), 6)
        self.assertEqual(ppcm(-12, 18), 36.0)
    
    def test_chaines_complexes(self):
        # Test avec chaînes complexes
        texte_complexe = "Le cheval de mon cousin est malade"
        self.assertEqual(compterVoyelles(texte_complexe), 12)
        self.assertEqual(compterlettre(texte_complexe, "e"), "Il y'a 5 fois e")

def run_all_tests():
    """Fonction pour exécuter tous les tests"""
    # Créer une suite de tests
    test_suite = unittest.TestSuite()
    
    # Ajouter toutes les classes de test
    test_classes = [
        TestArithmetique,
        TestTrigonometric,
        TestTableaux,
        TestPolynomes,
        TestChainesCaracteres,
        TestIntegrationNumerique,
        TestEquationsNonLineaires,
        TestConversions,
        TestFonctionsComplexes
    ]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)
    
    # Exécuter les tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    return result.wasSuccessful()

if __name__ == '__main__':
    print("🧪 Lancement des tests unitaires complets pour MathCraft...")
    print("=" * 60)
    
    success = run_all_tests()
    
    print("=" * 60)
    if success:
        print("🎉 Tous les tests ont réussi ! MathCraft est opérationnel.")
    else:
        print("❌ Certains tests ont échoué. Vérifie les fonctions concernées.")
    
    sys.exit(0 if success else 1)