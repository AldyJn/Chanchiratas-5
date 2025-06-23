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
        # Initialize empty adjacency list using dictionary
        # Key: vertex name, Value: list of adjacent vertices
        self.adjacency_list = {}
    
    def get_vertices(self):
        """
        Return list of all vertices in the graph.
        
        Time Complexity: O(V) where V is number of vertices
        Space Complexity: O(V) for creating new list
        
        Returns:
            list: All vertex names in the graph
        """
        # Extract all keys (vertex names) from adjacency list
        # Convert to list for consistent return type
        return list(self.adjacency_list.keys())
    
    def get_vertex_count(self):
        """
        Return the number of vertices in the graph.
        
        Time Complexity: O(1) - dictionary length is cached
        Space Complexity: O(1) - no additional space needed
        
        Returns:
            int: Number of vertices in graph
        """
        # Dictionary length gives us vertex count directly
        return len(self.adjacency_list)
    
    def has_vertex(self, vertex):
        """
        Check if a vertex exists in the graph.
        
        Time Complexity: O(1) - dictionary key lookup is average O(1)
        Space Complexity: O(1) - no additional space needed
        
        Args:
            vertex: The vertex to check for existence
            
        Returns:
            bool: True if vertex exists, False otherwise
        """
        # Use 'in' operator for dictionary key existence check
        # Handles empty graph case automatically (returns False)
        return vertex in self.adjacency_list

def test_1_1():
    """Test suite for basic graph foundation functionality."""
    
    # 1.1.1 Empty graph initialization
    graph = Graph()
    record_test("1.1.1 Empty graph initialization", graph.get_vertex_count() == 0)
    
    # 1.1.2 Vertex counting
    graph.adjacency_list = {"Lima": [], "Cusco": []}  # Simulate adding vertices
    record_test("1.1.2 Vertex counting", graph.get_vertex_count() == 2)
    
    # 1.1.3 Vertex existence check
    record_test("1.1.3 Vertex existence check", graph.has_vertex("Lima") == True)
    
    # 1.1.4 Empty graph edge case
    empty_graph = Graph()
    record_test("1.1.4 Empty graph edge case", empty_graph.has_vertex("Lima") == False)
    
    # 1.1.5 Type validation
    record_test("1.1.5 Type validation", isinstance(graph.get_vertices(), list))

# 🚀 Run tests
test_1_1()

# 📋 Summary
print("=== TEST RESULTS ===")
for r in test_results:
    print(r)

# 📊 Additional demonstration
print("\n=== DEMONSTRATION ===")
demo_graph = Graph()
print(f"Empty graph vertices: {demo_graph.get_vertices()}")
print(f"Empty graph count: {demo_graph.get_vertex_count()}")
print(f"Has vertex 'A': {demo_graph.has_vertex('A')}")

# Simulate adding vertices for demonstration
demo_graph.adjacency_list = {"A": [], "B": [], "C": []}
print(f"\nAfter adding vertices: {demo_graph.get_vertices()}")
print(f"Vertex count: {demo_graph.get_vertex_count()}")
print(f"Has vertex 'B': {demo_graph.has_vertex('B')}")
print(f"Has vertex 'D': {demo_graph.has_vertex('D')}")