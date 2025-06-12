import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.DiGraph()

    def creaGrafo(self, store, days):
        self._graph.clear()
        self._orders = DAO.getOrdersStore(store)
        self._idMapOrders = {}
        for o in self._orders:
            self._idMapOrders[o.order_id] = o
        self._graph.add_nodes_from(self._orders)
        self.addEdges(store, days)

    def addEdges(self, store, days):
        for o1_id, o2_id in DAO.getArchi(store, days):
            o1 = self._idMapOrders[o1_id]
            o2 = self._idMapOrders[o2_id]
            if o1!=o2 and not self._graph.has_edge(o2, o1) and not self._graph.has_edge(o1, o2):
                self._graph.add_edge(o1, o2)

    # def getLongestPath(self, s):
    #     if nx.is_directed_acyclic_graph(self._graph):
    #         path = nx.dag_longest_path(self._graph)
    #         print("Cammino più lungo:", [o.order_id for o in path])
    #     else:
    #         print("Errore: il grafo contiene cicli, impossibile usare dag_longest_path.")
    #


    def getAllStores(self):
        return DAO.getAllStores()


    def getNum(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

