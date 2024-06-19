# Espaco reservado para voce inserir suas variaveis globais.
# Voce pode inserir como funcao (exemplo): 
# 
#  my_global_variable = 'Awesome value'
#  def get_my_global_variable():
#       global my_global_variable
#       return my_global_variable

global lock_call # Lock para o totem
global chegou_cliente # Condition para o totem (chegou cliente)
global totem # Totem
global t_list # Lista de threads
global clients_lock # Lista de locks para os clientes
global clients_lock_cond # Lista de conditions para os clientes (clients_lock_cond[i] para o cliente i)
