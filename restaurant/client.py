# imports do Python
from threading import Thread
from time import sleep
from restaurant.totem import *

# imports do projeto

"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Client(Thread):
    
    """ Inicializa o cliente."""
    def __init__(self, i):
        self._id = i
        self._ticket = None
        super().__init__()
        # Insira o que achar necessario no construtor da classe.

    """ Pega o ticket do totem."""
    def get_my_ticket(self):
        self._ticket = totem.get_ticket()
        print("[TICKET] - O cliente {} pegou o ticket.".format(self._id))

    """ Espera ser atendido pela equipe. """
    def wait_crew(self):
        print("[WAIT] - O cliente {} esta aguardando atendimento.".format(self._id))
        with clients_lock[self._id]:
            clients_lock_cond[self._id].wait()

    """ O cliente pensa no pedido."""
    def think_order(self):
        print("[THINK] - O cliente {} esta pensando no que pedir.".format(self._id))
        sleep(randint(1, 5))

    """ O cliente faz o pedido."""
    def order(self):
        print("[ORDER] - O cliente {} pediu algo.".format(self._id))
        with clients_lock[self._id]:
            chegou_cliente.notify()

    """ Espera pelo pedido ficar pronto. """
    def wait_chef(self):
        print("[WAIT MEAL] - O cliente {} esta aguardando o prato.".format(self._id))
        with clients_lock[self._id]:
            clients_lock_cond[self._id].wait()
    
    """
        O cliente reserva o lugar e se senta.
        Lembre-se que antes de comer o cliente deve ser atendido pela equipe, 
        ter seu pedido pronto e possuir um lugar pronto pra sentar. 
    """
    def seat_and_eat(self):
        print("[WAIT SEAT] - O cliente {} esta aguardando um lugar ficar livre".format(self._id))
        table.seat(self)
        with clients_lock[self._id]:
            clients_lock_cond[self._id].notify()
        print("[SEAT] - O cliente {} encontrou um lugar livre e sentou".format(self._id))
        sleep(randint(1, 5))

    """ O cliente deixa o restaurante."""
    def leave(self):
        with clients_lock[self._id]:
            clients_lock_cond[self._id].wait()
        table.leave(self)
        print("[LEAVE] - O cliente {} saiu do restaurante".format(self._id))
    
    """ Thread do cliente """
    def run(self):
        self.get_my_ticket()
        self.wait_crew()
        self.think_order()
        self.order()
        self.wait_chef()
        self.seat_and_eat()
        self.leave()