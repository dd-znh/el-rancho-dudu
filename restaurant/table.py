
"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""

from restaurant.shared import *

class Table:

    """ Inicia a mesa com um número de lugares """
    def __init__(self,number):
        self._number = number
        # Insira o que achar necessario no construtor da classe.
    
    """ O cliente se senta na mesa."""
    def seat(self, client):
        sem_tab.acquire()
    
    """ O cliente deixa a mesa."""
    def leave(self, client):
        sem_tab.release()
