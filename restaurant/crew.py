# imports do Python
from threading import Thread
import restaurant.shared as shared


"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Crew(Thread):
    
    """ Inicia o membro da equipe com um id (use se necessario)."""
    def __init__(self, id):
        super().__init__()
        self._id = id
        self._ticket_atual = None
        # Insira o que achar necessario no construtor da classe.

    """ O membro da equipe espera um cliente. """    
    def wait(self):
        print("O membro da equipe {} está esperando um cliente.".format(self._id))

        # Espera um cliente chegar
        shared.sem_totem.acquire()

    """ O membro da equipe chama o cliente da senha ticket."""
    def call_client(self, ticket):

        # Remove o ticket da lista de chamadas do totem
        with shared.totem_lock:
            shared.totem.call.remove(ticket)

        print("[CALLING] - O membro da equipe {} está chamando o cliente da senha {}.".format(self._id, ticket))

        # Libera o cliente com o ticket atual atualizado
        self._ticket_atual = ticket
        shared.sem_wait_crew[ticket].release()

    def make_order(self, order): 
        # Espera o cliente fazer o pedido
        shared.sem_wait_client[self._ticket_atual].acquire()

        print("[STORING] - O membro da equipe {} está anotando o pedido {} para o chef.".format(self._id, order))

        # Coloca o pedido na fila do chef
        with shared.lock_chef:
            shared.fila_pedidos_chef.put(order)
            shared.cond_chef.notify()

    """ Thread do membro da equipe."""
    def run(self):
        self.wait()
        # Enquanto houver clientes para atender são executadas as funções de chamar cliente e fazer pedido
        while (1):
            with shared.totem_lock: # lock do totem para acessar o número de clientes restantes
                if shared.clients_remain == 0:
                    break
                shared.clients_remain -= 1
                min_ticket = min(shared.totem.call)
            self.call_client(min_ticket)
            self.make_order(self._ticket_atual)            
