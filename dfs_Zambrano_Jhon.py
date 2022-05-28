
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


    def print_lista_adyacente(self):
        """
        Una lista de adyacencia es un tipo de representación gráfica en código, consiste en llaves que representan cada nodo, y un colocar de valores
        para cada uno de ellos que contienen nodos que están conectados al nodo clave con un 
        borde.
        """
        for key in self.m_lista_adyacencia.keys():
            print("nodo:    ", key, ": ", self.m_lista_adyacencia[key])
        """
        si nos encontramos fuera de la for bucle, significa que todas las ramas vecinas
        del nodo actual han sido visitadas
        y ninguna de ellas conduce a nuestro nodo de destino.
        """    
    def dfs(self, comienzo, objetivo, camino=[], nodo_visitado=set()):
        """
        Usaremos el método recursivo para implementar dfs de la implentación 
        de la búsqueda.
        Agregamos el nodo de inicio al comienzo de nuestra ruta transversal y 
        lo marcamos como visited añadiéndolo a un conjunto de visitos de nodos.

        Parametros:
            comienzo (tipo): descripcion
            comienzo (tipo): descripcion
            path (lista, opcional): Por defecto se guardará en una lista[]
            nodo_visitado (tipo, opcional): descripcion: en esta parte se setea

        Retorna:
            none 
        """
        camino.append(
            comienzo)  # Append() Este método nos permite agregar nuevos elementos a una lista.
        nodo_visitado.add(comienzo)  # nodo visitado se agrega al comienzo
        if comienzo == objetivo:  # Si el comienzo es igual al objetivo
            return camino  # retorna el camino

        # for bucle, significa que todas las ramas vecinas del
        for (nodos_no_visitados, weight) in self.m_lista_adyacencia[comienzo]:
            # nodo actual y
            # ninguna de ellas conduce a nuestro nodo de destino

            if nodos_no_visitados not in nodo_visitado:  # Si los nodos no visitados.
                # El operador not devuelve el valor opuesto la valor booleano.
                # el resultado será =
                resultado = self.dfs(nodos_no_visitados,
                                     objetivo, camino, nodo_visitado)
                # al metodo self y como parametro se envia a los nodos no visitado, objetivo, camino y nodo visitado.
                if resultado is not None:  # si el resultado no tiene una falta de valor, esto objeto no tiene métodos
                    return resultado  # retorna el resultado
        # El método pop() elimina y retorna un elemento de una lista.
        camino.pop()
        return None
if __name__ == "__main__":
    #### METODO MAIN PARA LLAMAR A LA CLASE #####