# registry/urls.py
from django.urls import path
from .views import register_agent, list_agents

urlpatterns = [
    path("api/agents/register", register_agent),
    path("api/agents/list", list_agents),
]