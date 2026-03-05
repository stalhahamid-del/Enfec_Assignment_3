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


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Agent

@api_view(["GET"])
def search_agents(request):
    capability = request.GET.get("capability")

    if not capability:
        return Response({"error": "capability parameter required"}, status=400)

    agents = Agent.objects.filter(capabilities__contains=[capability])

    data = []
    for agent in agents:
        data.append({
            "id": agent.id,
            "name": agent.name,
            "description": agent.description,
            "capabilities": agent.capabilities,
            "endpoint_url": agent.endpoint_url,
            "status": agent.status
        })

    return Response(data)
