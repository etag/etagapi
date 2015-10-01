from django.shortcuts import render
#from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets, filters
from rest_framework.renderers import BrowsableAPIRenderer, JSONPRenderer,JSONRenderer,XMLRenderer,YAMLRenderer #, filters
#from renderer import CustomBrowsableAPIRenderer
from filters import ReadersFilter
from etag.models import Readers
from serializer import ReaderSerializer


class ReadersViewSet(viewsets.ModelViewSet):
    """
    This is the roost list with source table hyperlinked.
    """
    model = Readers
    queryset = Readers.objects.all()
    serializer_class = ReaderSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter) #,filters.OrderingFilter)
    filter_class = ReadersFilter
    search_fields = ('name', 'description',)
    #ordering_fields = ('name', 'description', 'latitude', 'longitude', 'source_no','source__cource')
