# 🧪 Lista para resultados de prueba
test_results = []

def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

# 📦 Clase del Grafo con análisis avanzado
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
        if vertex1 not in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex2].append(vertex1)

    def get_degree(self, vertex):
        # Retorna el número de conexiones del vértice
        if vertex in self.adjacency_list:
            return len(self.adjacency_list[vertex])
        return 0  # o también puede usarse None

    def find_all_paths(self, start_vertex, end_vertex, max_length=None):
        # Encuentra todos los caminos posibles entre start y end usando DFS

        # Si alguno no existe, no hay caminos
        if start_vertex not in self.adjacency_list or end_vertex not in self.adjacency_list:
            return []

        paths = []

        def dfs(current, end, path):
            # Si la longitud supera el máximo, se detiene
            if max_length is not None and len(path) > max_length:
                return
            if current == end:
                paths.append(path)
                return
            for neighbor in self.adjacency_list.get(current, []):
                if neighbor not in path:
                    dfs(neighbor, end, path + [neighbor])

        dfs(start_vertex, end_vertex, [start_vertex])
        return paths

    def get_connected_components(self):
        # Retorna lista de componentes conectados (cada uno es una lista de vértices)
        visited = set()
        components = []

        for vertex in self.adjacency_list:
            if vertex not in visited:
                component = []
                queue = [vertex]
                visited.add(vertex)
                while queue:
                    current = queue.pop(0)
                    component.append(current)
                    for neighbor in self.adjacency_list[current]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                components.append(component)

        return components

# 🚀 Función de prueba completa
def test_1_5():
    graph = Graph()

    # Crear grafo de prueba
    graph.add_edge("Lima", "Cusco")
    graph.add_edge("Lima", "Arequipa")
    graph.add_edge("Cusco", "Arequipa")
    graph.add_edge("Trujillo", "Piura")  # Componente separado

    # 1.5.1 Grado del vértice
    lima_degree = graph.get_degree("Lima")
    record_test("1.5.1 Degree calculation", lima_degree == 2)

    # 1.5.2 Encontrar múltiples caminos
    paths = graph.find_all_paths("Lima", "Arequipa", max_length=3)
    has_multiple_paths = len(paths) >= 2
    record_test("1.5.2 Multiple paths finding", has_multiple_paths)

    # 1.5.3 Componentes conectados
    components = graph.get_connected_components()
    has_two_components = len(components) == 2
    record_test("1.5.3 Connected components", has_two_components)

    # 1.5.4 Análisis de grafo vacío
    empty_graph = Graph()
    empty_components = empty_graph.get_connected_components()
    record_test("1.5.4 Empty graph analysis", empty_components == [])

    # 1.5.5 Manejo de vértices inexistentes
    degree = graph.get_degree("NonExistent")
    record_test("1.5.5 Non-existent vertex handling", degree == 0)

# 🧪 Ejecutar pruebas
test_1_5()

# 📋 Mostrar resultados
for r in test_results:
    print(r)