# coding: utf-8

from source.classifica_senha import ClassificaSenha
import unittest

class TesteClassificaSenha(unittest.TestCase):
    def test_ClassificaSenha_senha(self):
        """
        Método para teste da ClassificaSenhação
        """
        print("Testando...")
        self.assertFalse(ClassificaSenha("1234567").classifica_senha())  # menor que min de char não é aceito
        self.assertEqual(ClassificaSenha('12345678').classifica_senha(), 0)  # min de char, apenas num, fraco
        self.assertEqual(ClassificaSenha('abcdefgh').classifica_senha(), 0)  # min de char, apenas str, fraco
        self.assertEqual(ClassificaSenha('!@#$%!@$').classifica_senha(), 0)  # min de char, apenas especial, fraco
        self.assertEqual(ClassificaSenha('Testando1').classifica_senha(), 1)  # min char, str e num, médio
        self.assertEqual(ClassificaSenha('Testando@').classifica_senha(), 1)  # min char, str e especial, médio
        self.assertEqual(ClassificaSenha('!@#$%!@123').classifica_senha(), 1)  # min char, num e especial, médio
        self.assertFalse(ClassificaSenha('123qwe').classifica_senha())  # menor que min de char, str e num, inválido
        self.assertFalse(ClassificaSenha('123@@@').classifica_senha())  # menor que min de char, num e especial, inválido
        self.assertFalse(ClassificaSenha('qwe@@@').classifica_senha())  # menor que min de char, str e especial, inválido
        self.assertFalse(ClassificaSenha('Testan1').classifica_senha())  # menor que min de char, dois tipos, não válido
        self.assertEqual(ClassificaSenha('Testando1!').classifica_senha(), 2)  # maior que min de char, três tipos, forte
        self.assertFalse(ClassificaSenha('12@@TT').classifica_senha())  # menor que min de char, três tipos, inválido

if __name__ == '__main__':
    unittest.main()

