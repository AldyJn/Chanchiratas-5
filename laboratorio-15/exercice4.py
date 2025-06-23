# 🧪 Lista para registrar resultados de pruebas
test_results = []

# ✅ Función para registrar si cada prueba pasó o no
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

# 📦 Clase del Grafo
class Graph:
    def __init__(self):
        # Diccionario que representa el grafo (lista de adyacencia)
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        # Agrega vértice si no existe
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        # Asegura que ambos vértices existan
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        # Conecta ambos si no están conectados ya (no duplicar)
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
        if vertex1 not in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex2].append(vertex1)
    
    def find_path(self, start_vertex, end_vertex):
        # Retorna el camino más corto entre start y end usando BFS
        
        # Caso especial: buscarse a sí mismo
        if start_vertex == end_vertex:
            return [start_vertex]
        
        # Cola para BFS: cada elemento es (vértice actual, camino hasta ese vértice)
        queue = [(start_vertex, [start_vertex])]
        
        # Conjunto de visitados para no repetir vértices
        visited = set()
        
        while queue:
            current, path = queue.pop(0)  # Tomar el primero en la cola
            visited.add(current)
            
            for neighbor in self.adjacency_list.get(current, []):
                if neighbor == end_vertex:
                    return path + [neighbor]
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
                    visited.add(neighbor)
        
        # Si no se encontró camino
        return []

    def is_connected(self, vertex1, vertex2):
        # Retorna True si hay camino entre vertex1 y vertex2, usando find_path
        return len(self.find_path(vertex1, vertex2)) > 0

# 🚀 Función para correr todos los tests del reto
def test_1_4():
    graph = Graph()
    
    # Crear grafo de prueba: Lima - Cusco - Arequipa
    graph.add_edge("Lima", "Cusco")
    graph.add_edge("Cusco", "Arequipa")
    graph.add_vertex("Trujillo")  # Nodo aislado
    
    # 1.4.1 Camino directo
    path = graph.find_path("Lima", "Cusco")
    record_test("1.4.1 Direct connection path", path == ["Lima", "Cusco"])
    
    # 1.4.2 Camino indirecto (Lima → Cusco → Arequipa)
    path = graph.find_path("Lima", "Arequipa")
    is_valid_path = len(path) == 3 and path[0] == "Lima" and path[-1] == "Arequipa"
    record_test("1.4.2 Indirect connection path", is_valid_path)
    
    # 1.4.3 Sin camino posible
    path = graph.find_path("Lima", "Trujillo")
    record_test("1.4.3 No path case", path == [])
    
    # 1.4.4 Camino a sí mismo
    path = graph.find_path("Lima", "Lima")
    record_test("1.4.4 Self path", path == ["Lima"])
    
    # 1.4.5 Verificación de conectividad
    connected = graph.is_connected("Lima", "Arequipa")
    not_connected = graph.is_connected("Lima", "Trujillo")
    record_test("1.4.5 Connectivity check", connected and not not_connected)

# 🧪 Ejecutar pruebas
test_1_4()

# 📋 Mostrar resultados
for r in test_results:
    print(r)