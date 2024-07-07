# Espaco reservado para voce inserir suas variaveis globais.
# Voce pode inserir como funcao (exemplo): 
# 
#  my_global_variable = 'Awesome value'
#  def get_my_global_variable():
#       global my_global_variable
#       return my_global_variable

global sem_totem # Semaforo para o totem (chegou cliente)
sem_totem = None
global clients_remain # Variável para controlar o número de clientes
clients_remain = None

global totem # Totem
totem = None
global table # Mesa
table = None

global sem_tab # Semáforo para acesso a mesa
sem_tab = None

global totem_lock # Lock para operação do Totem
totem_lock = None

global sem_wait_client # Semáforo para o cliente
sem_wait_client = {}
global sem_wait_chef # Semáforo para o chef
sem_wait_chef = {}
global sem_wait_crew # Semáforo para a equipe
sem_wait_crew = {}

global fila_pedidos_chef # Lista de pedidos para o chef
fila_pedidos_chef = None
global lock_chef # Lock para a lista de pedidos do chef
lock_chef = None
global cond_chef # Condition para o chef
cond_chef = None

global n_clients# número de clientes
n_clients = None