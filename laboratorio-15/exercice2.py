test_results = []

def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Graph:
    def __init__(self):
        """
        Initialize empty adjacency list representation of graph.
        
        Time Complexity: O(1) - constant time initialization
        Space Complexity: O(1) - only creates empty dictionary
        """
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph with an empty adjacency list.
        Prevents duplicate vertices by checking existence first.
        
        Time Complexity: O(1) average case - dictionary key lookup and insertion
        Space Complexity: O(1) - adds one key-value pair to dictionary
        
        Args:
            vertex: The vertex identifier to add to the graph
            
        Returns:
            None - modifies graph in place
        """
        # Step 1: Check if vertex already exists to prevent duplicates
        # This is crucial for maintaining graph integrity and preventing
        # accidental overwrites of existing adjacency lists
        if vertex not in self.adjacency_list:
            # Step 2: Add vertex with empty adjacency list
            # Empty list represents an isolated vertex with no connections
            # This preserves the adjacency list structure for future edge additions
            self.adjacency_list[vertex] = []
        
        # Note: If vertex already exists, we do nothing (duplicate prevention)
        # This ensures idempotent behavior - adding same vertex multiple times
        # has the same effect as adding it once
    
    def get_vertices(self):
        """
        Return list of all vertices in the graph.
        
        Time Complexity: O(V) where V is number of vertices
        Space Complexity: O(V) for creating new list
        """
        return list(self.adjacency_list.keys())
    
    def get_vertex_count(self):
        """
        Return the number of vertices in the graph.
        
        Time Complexity: O(1) - dictionary length is cached
        Space Complexity: O(1) - no additional space needed
        """
        return len(self.adjacency_list)
    
    def has_vertex(self, vertex):
        """
        Check if a vertex exists in the graph.
        
        Time Complexity: O(1) average case - dictionary key lookup
        Space Complexity: O(1) - no additional space needed
        """
        return vertex in self.adjacency_list

def test_1_2():
    """Test suite for vertex addition functionality."""
    graph = Graph()
    
    # 1.2.1 Single vertex addition
    graph.add_vertex("Lima")
    record_test("1.2.1 Single vertex addition", graph.has_vertex("Lima"))
    
    # 1.2.2 Multiple vertex addition
    graph.add_vertex("Cusco")
    graph.add_vertex("Arequipa")
    record_test("1.2.2 Multiple vertex addition", graph.get_vertex_count() == 3)
    
    # 1.2.3 Duplicate prevention
    initial_count = graph.get_vertex_count()
    graph.add_vertex("Lima")  # Adding duplicate
    record_test("1.2.3 Duplicate prevention", graph.get_vertex_count() == initial_count)
    
    # 1.2.4 Vertex isolation
    lima_neighbors = graph.adjacency_list.get("Lima", [])
    record_test("1.2.4 Vertex isolation", len(lima_neighbors) == 0)
    
    # 1.2.5 Graph size tracking
    graph.add_vertex("Trujillo")
    record_test("1.2.5 Graph size tracking", "Trujillo" in graph.get_vertices())

# 🚀 Run tests
test_1_2()

# 📋 Summary
print("=== TEST RESULTS ===")
for r in test_results:
    print(r)

# 📊 Additional demonstration
print("\n=== VERTEX ADDITION DEMONSTRATION ===")
demo_graph = Graph()

print("Step 1: Empty graph")
print(f"Vertices: {demo_graph.get_vertices()}")
print(f"Count: {demo_graph.get_vertex_count()}")

print("\nStep 2: Adding first vertex 'A'")
demo_graph.add_vertex("A")
print(f"Vertices: {demo_graph.get_vertices()}")
print(f"Count: {demo_graph.get_vertex_count()}")
print(f"A's neighbors: {demo_graph.adjacency_list['A']}")

print("\nStep 3: Adding multiple vertices")
demo_graph.add_vertex("B")
demo_graph.add_vertex("C")
demo_graph.add_vertex("D")
print(f"Vertices: {demo_graph.get_vertices()}")
print(f"Count: {demo_graph.get_vertex_count()}")

print("\nStep 4: Attempting to add duplicate 'A'")
print(f"Count before: {demo_graph.get_vertex_count()}")
demo_graph.add_vertex("A")  # Should not increase count
print(f"Count after: {demo_graph.get_vertex_count()}")
print(f"A's neighbors unchanged: {demo_graph.adjacency_list['A']}")

print("\nStep 5: Final adjacency list structure")
for vertex, neighbors in demo_graph.adjacency_list.items():
    print(f"'{vertex}': {neighbors}")