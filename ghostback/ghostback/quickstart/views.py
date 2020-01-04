from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from ghostback.quickstart import models, serializers

# Create your views here.
class RoastBoastViewset(viewsets.ModelViewSet):
    queryset = models.RoastBoast.objects.all()
    serializer_class = serializers.RoastBoastSerializer
