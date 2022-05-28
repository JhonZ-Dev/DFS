
'''
Es especialmente util en la programacion en hilo cuando la informacion 
debe intercambiarse de forma segura entre varios subprocesos. 
La clase Queue de este
modulo implementa toda la semantica de bloqueo necesaria.
'''
from queue import Queue

class Grafo:  # Creamos una clase grafo, la cual tendra otras funciones dentro de esta clase denominada graph o grafo
    # se crea un objeto o instancia de una clase, se llama al constructor ( __init__())
    def __init__(self, numeros_de_nodos, nodo_dirigido=True):
        # Al crear una instancia de una clase, necesitamos diferenciar o especificar los atributos de la instancia de los argumentos y otras variables.
        # Y ahí es donde necesitamos la palabra clave
        """
        __init__() El método define un constructor. 
        Consiste en un número de nodos,
        un metodos self(uno mismo)
        un conjunto de nodos y el representación gráfica.

        Parametros:
            numero de nodos (_tipo_): _descripcion_
            nodo_dirigido (booleano, optcinal): Por defecto valor verdadero.
            self(uno miso): para especificar que estamos pasando el valor a 
            los atributos de la instancia y no a la variable o 
            argumento local con el mismo nombre.
        """
        self.m_num_of_nodes = numeros_de_nodos  # No hay numero nodo o si hay numero de nodos
        # Coloca en un definido rango el numero de nodos
        self.m_nodos = range(self.m_num_of_nodes)
        self.m_nodo_dirigido = nodo_dirigido  # Nodo dirigido o no dirigido
        # Se crea una lista de adyacencia #Se crea un diccionario con cada nodo del gráfico configurado para ser una clave
        # En es parte optimizamos el códgo implementado un for
        self.m_lista_adyacencia = {nodo: set() for nodo in self.m_nodos}
