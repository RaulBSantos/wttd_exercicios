import unittest


def _is_cakeable(recipe: dict, available: dict):
    """Verifica se dada uma receita e os ingredientes, se é 'bolível'
       fazer um bolo...
    """
    return set(recipe).issubset(set(available))


def cakes(recipe: dict, available: dict):
    """Calcula qual a quantidade mínima de bolos que podem ser feitos
       com a receita e os ingredientes disponíveis.
    """
    if not _is_cakeable(recipe, available):
        return 0
    qnt_min = float('inf')
    for ingr in recipe.keys():
        mult = available[ingr] // recipe[ingr]
        if mult < qnt_min:
            qnt_min = mult
    return qnt_min


class TestCakes(unittest.TestCase):
    def test_cakeable(self):
        self.assertEqual(True, _is_cakeable({'apple': 1, 'milk': 2},
                                           {'apple': 2, 'milk': 3}))
        self.assertEqual(False, _is_cakeable({'egg': 12, 'apple': 1, 'milk': 2},
                                            {'apple': 2, 'milk': 3}))

    def test_cakes(self):
        self.assertEqual(2, cakes(
            {'flour': 500, 'sugar': 200, 'eggs': 1},
            {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))
        self.assertEqual(0, cakes(
            {'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100},
            {'sugar': 500, 'flour': 2000, 'milk': 2000}))

        self.assertEqual(1, cakes(
            {'flour': 500, 'sugar': 200},
            {'flour': 600, 'sugar': 1200}))
        self.assertEqual(0, cakes(
            {'flour': 700, 'sugar': 200},
            {'flour': 600, 'sugar': 1200}))


if __name__ == '__main__':
    unittest.main()
