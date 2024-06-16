from django.shortcuts import render

# Create your views here.
# graph_solver/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Graph

class AStarView(APIView):
    def post(self, request):
        data = request.data
        vertices = data.get('vertices')
        edges = data.get('edges')
        start_vertex = data.get('start_vertex')
        end_vertex = data.get('end_vertex')

        graph = Graph(vertices, edges)
        #solution = graph.astar(start_vertex, end_vertex)

        return Response({'solution': 'YOU HAVE WON!!!'})
