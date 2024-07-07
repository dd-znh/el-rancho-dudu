# imports do Python
from threading import Thread
from time import sleep
from random import randint
from queue import Queue
import restaurant.shared as shared

"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Chef(Thread):
    
    def __init__(self):
        self._ticket_atual = None
        self.n_pratos = 0
        super().__init__()
        # Insira o que achar necessario no construtor da classe.

    """ Chef prepara um dos pedido que recebeu do membro da equipe."""
    def cook(self):
        print("[COOKING] - O chefe esta preparando o pedido para a senha {}.".format(self._ticket_atual)) # Modifique para o numero do ticket
        sleep(randint(1,5))

    """ Chef serve o pedido preparado."""
    def serve(self):
        print("[READY] - O chefe está servindo o pedido para a senha {}.".format(self._ticket_atual)) # Modificar para o numero do ticket
        # Libera o cliente
        shared.sem_wait_chef[self._ticket_atual].release()
    
    """ O chefe espera algum pedido vindo da equipe."""
    def wait_order(self):
        with shared.lock_chef: # lock na fila de pedidos
            # Se a fila de pedidos estiver vazia, o chefe espera
            if (shared.fila_pedidos_chef.empty()):
                print("O chefe está esperando algum pedido.")
                shared.cond_chef.wait()
            # Senão, pega o pedido da fila
            self._ticket_atual = shared.fila_pedidos_chef.get()

    """ Thread do chefe."""
    def run(self):
        # Enquanto houver clientes
        while self.n_pratos != shared.n_clients:
            self.wait_order()
            self.cook()
            self.serve()
            self.n_pratos += 1