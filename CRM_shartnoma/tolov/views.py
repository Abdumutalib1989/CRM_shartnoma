from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Tolov
from .serializers import TolovSerializer


class TolovListCreateAPIView(ListCreateAPIView):
    queryset = Tolov.objects.all()
    serializer_class = TolovSerializer

class TolovGetUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Tolov.objects.all()
    serializer_class = TolovSerializer