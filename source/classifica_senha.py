# coding: utf-8

import re

class ClassificaSenha:
    def __init__(self, pwd):
        self.pwd = pwd

    def classifica_senha(self):
        """
        Método para a classificação de senha. São requeridos um minimo de 8 caracteres para a senha ser aceita.
        Ser minimamente aceita a classifica como fraca, para média e forte deve-se fazer uso de números e caracteres
        especiais. Uma senha de 9 caracteres no total contendo num, letras e simbolos é forte. O mesmo caso usando
        letras e números apenas é classificada como média.
        """
        if len(self.pwd) > 7:

