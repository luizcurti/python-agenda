from rest_framework import generics
from ..models import Contact
from .serializers import ContactSerializer


class ContactListCreateAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.filter(visible=True).order_by('-id')
    serializer_class = ContactSerializer


class ContactRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
