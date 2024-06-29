# imports do Python
from threading import Thread
from restaurant.shared import *


"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Crew(Thread):
    
    """ Inicia o membro da equipe com um id (use se necessario)."""
    def __init__(self, id):
        super().__init__()
        self._id = id
        self._cliente_atual = None
        # Insira o que achar necessario no construtor da classe.

    """ O membro da equipe espera um cliente. """    
    def wait(self):
        print("O membro da equipe {} está esperando um cliente.".format(self._id))

        # Espera o cliente chegar
        chegou_cliente.wait()

    """ O membro da equipe chama o cliente da senha ticket."""
    def call_client(self, ticket):

        # Remove o ticket da lista de chamadas do totem
        totem.call.remove(ticket)

        print("[CALLING] - O membro da equipe {} está chamando o cliente da senha {}.".format(self._id, ticket))

        # Libera o cliente
        for t in t_list:
            if isinstance(t, Client) and t._ticket == ticket:
                self._cliente_atual = t
                with clients_lock[t._id]:
                    clients_lock_cond[ticket].notify()
        
        # Espera o cliente terminar o pedido
        with lock_call:
            chegou_cliente.wait()
        

    def make_order(self, order):
        print("[STORING] - O membro da equipe {} está anotando o pedido {} para o chef.".format(self._id, order))
        with lock_chef:
            lista_pedidos_chef.append(order)
            lock_chef.notify()

    """ Thread do membro da equipe."""
    def run(self):
        self.wait()
        self.call_client(min(totem.call))
        self.make_order(self._cliente_atual._ticket)
