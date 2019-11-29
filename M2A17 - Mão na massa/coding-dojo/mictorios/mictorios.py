import unittest


def organiza_mictorios(mictorios: int, ocupados: list) -> tuple:
    """Deve retornar uma tupla(int, list)) com a quantidade de mijões
       que cabem no mictório (int) e as posições para eles utilizarem sem
       constrangimento (lista de int).
    """
    sem_constrangimento = []
    for posicao in range(1, mictorios + 1):
        if not tem_constrangimento(posicao, (sem_constrangimento + ocupados)):
            sem_constrangimento.append(posicao)

    return (len(sem_constrangimento), sem_constrangimento)


def tem_constrangimento(posicao, ocupados):
    """Dada uma posição e os mictórios já ocupados, retorna se a posição
       geraria constrangimento se fosse ocupada.
    """
    if posicao in ocupados:
        return True
    return (posicao + 1) in ocupados or (posicao - 1) in ocupados


class TestMictorios(unittest.TestCase):
    def test_framework(self):
        self.assertTrue(True)

    def test_tem_constrangimento(self):
        self.assertEqual(tem_constrangimento(posicao=2, ocupados=[1, 3]), True)
        self.assertEqual(tem_constrangimento(posicao=1, ocupados=[1, 3]), True)
        self.assertEqual(tem_constrangimento(posicao=5, ocupados=[1, 3]), False)
        self.assertEqual(tem_constrangimento(posicao=1, ocupados=[3, 5]), False)

    def test_organiza_mictorios(self):
        self.assertEqual(organiza_mictorios(mictorios=3,
                                            ocupados=[1, 3]), (0, []))
        self.assertEqual(organiza_mictorios(mictorios=10,
                                            ocupados=[1, 3]), (3, [5, 7, 9]))
        self.assertEqual(organiza_mictorios(mictorios=9,
                                            ocupados=[2, 4, 6, 8]), (0, []))
        self.assertEqual(organiza_mictorios(mictorios=10,
                                            ocupados=[2, 4, 6, 8]), (1, [10]))


if __name__ == '__main__':
    unittest.main()
