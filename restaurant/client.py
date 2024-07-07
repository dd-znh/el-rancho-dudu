# imports do Python
from random import randint
from threading import Condition, Lock, Semaphore, Thread
from time import sleep
import restaurant.shared as shared

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
        with shared.totem_lock: # lock no totem
            self._ticket = shared.totem.get_ticket() # pega um ticket
        shared.sem_wait_crew[self._ticket] = Semaphore(0) # cria um semáforo para a espera da equipe
        shared.sem_wait_client[self._ticket] = Semaphore(0) # cria um semáforo para liberar o atendente anotar seu pedido
        shared.sem_wait_chef[self._ticket] = Semaphore(0) # cria um semáforo para esperar o pedido ficar pronto
        print("[TICKET] - O cliente {} pegou o ticket.".format(self._id))

    """ Espera ser atendido pela equipe. """
    def wait_crew(self):
        print("[WAIT] - O cliente {} esta aguardando atendimento.".format(self._id))
        # uso do semáforo para esperar a equipe
        shared.sem_wait_crew[self._ticket].acquire()

    """ O cliente pensa no pedido."""
    def think_order(self):
        print("[THINK] - O cliente {} esta pensando no que pedir.".format(self._id))
        sleep(randint(1, 5))

    """ O cliente faz o pedido."""
    def order(self):
        # uso do semáforo para liberar o atendente anotar o pedido
        shared.sem_wait_client[self._ticket].release()
        print("[ORDER] - O cliente {} pediu algo.".format(self._id))

    """ Espera pelo pedido ficar pronto. """
    def wait_chef(self):
        print("[WAIT MEAL] - O cliente {} esta aguardando o prato.".format(self._id))
        # uso do semáforo para esperar o pedido ficar pronto
        shared.sem_wait_chef[self._ticket].acquire()

    """
        O cliente reserva o lugar e se senta.
        Lembre-se que antes de comer o cliente deve ser atendido pela equipe, 
        ter seu pedido pronto e possuir um lugar pronto pra sentar. 
    """
    def seat_and_eat(self):
        print("[WAIT SEAT] - O cliente {} esta aguardando um lugar ficar livre".format(self._id))
        # chama a função de sentar na mesa
        shared.table.seat(self)
        print("[SEAT] - O cliente {} encontrou um lugar livre e sentou".format(self._id))
        sleep(randint(1, 5))

    """ O cliente deixa o restaurante."""
    def leave(self):
        # chama a função de sair da mesa
        shared.table.leave(self)
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