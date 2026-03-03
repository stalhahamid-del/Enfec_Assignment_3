# registry/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Agent
from .serializers import AgentSerializer

@api_view(["POST"])
def register_agent(request):
    serializer = AgentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(["GET"])
def list_agents(request):
    agents = Agent.objects.all()
    serializer = AgentSerializer(agents, many=True)
    return Response(serializer.data)