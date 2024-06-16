from django.db import models

# Create your models here.
# graph_solver/models.py
class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        
        # Implement other necessary methods (heuristic, A* algorithm, etc.)
