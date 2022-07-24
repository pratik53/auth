from django.shortcuts import render
from .models import Project
from .serializer import ProjectSerailizer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class ProjectView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = Project
    queryset = Project.objects.all()