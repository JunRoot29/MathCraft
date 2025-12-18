from test import run_all_tests


def test_unittest_suite():
    # Exécute la suite de tests existante (unittest) et vérifie qu'elle réussit
    assert run_all_tests() is True
