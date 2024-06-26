from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

def index(request):
    return render(request, 'index.html', {})
