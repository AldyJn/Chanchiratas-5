test_results = []

# Función para registrar el resultado de cada test
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Graph:
    def __init__(self):
        # Diccionario para almacenar la lista de adyacencia (relaciones entre vértices)
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        # Agrega un vértice si no existe aún en la lista de adyacencia
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def has_vertex(self, vertex):
        # Verifica si el vértice existe en el grafo
        return vertex in self.adjacency_list

    def add_edge(self, vertex1, vertex2):
        # Si vertex1 no existe, se crea automáticamente
        if vertex1 not in self.adjacency_list:
            self.add_vertex(vertex1)
        # Si vertex2 no existe, se crea automáticamente
        if vertex2 not in self.adjacency_list:
            self.add_vertex(vertex2)
        
        # Evita duplicados: agrega vertex2 a la lista de vertex1 si aún no está
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
        
        # Evita duplicados: agrega vertex1 a la lista de vertex2 si aún no está
        if vertex1 not in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex2].append(vertex1)

    def has_edge(self, vertex1, vertex2):
        # Verifica si existe una conexión entre vertex1 y vertex2
        if vertex1 in self.adjacency_list:
            return vertex2 in self.adjacency_list[vertex1]
        return False

    def get_neighbors(self, vertex):
        # Devuelve la lista de vértices conectados al vértice dado
        return self.adjacency_list.get(vertex, [])

# Función de prueba para validar todos los casos del reto
def test_1_3():
    graph = Graph()
    
    # 1.3.1 Creación básica de arista
    graph.add_vertex("Lima")
    graph.add_vertex("Cusco")
    graph.add_edge("Lima", "Cusco")
    record_test("1.3.1 Basic edge creation", graph.has_edge("Lima", "Cusco"))
    
    # 1.3.2 Conexión bidireccional
    record_test("1.3.2 Bidirectional connection", graph.has_edge("Cusco", "Lima"))
    
    # 1.3.3 Creación automática de vértices
    graph.add_edge("Arequipa", "Trujillo")  # Ambos vértices deben crearse automáticamente
    has_both = graph.has_vertex("Arequipa") and graph.has_vertex("Trujillo")
    record_test("1.3.3 Auto vertex creation", has_both)
    
    # 1.3.4 Prevención de duplicados en aristas
    initial_neighbors = len(graph.get_neighbors("Lima"))
    graph.add_edge("Lima", "Cusco")  # No debe duplicar
    final_neighbors = len(graph.get_neighbors("Lima"))
    record_test("1.3.4 Duplicate edge prevention", initial_neighbors == final_neighbors)
    
    # 1.3.5 Verificación de conexión
    lima_neighbors = graph.get_neighbors("Lima")
    record_test("1.3.5 Connection verification", "Cusco" in lima_neighbors)

# 🚀 Ejecutar pruebas
test_1_3()

# 📋 Mostrar resultados
for r in test_results:
    print(r)