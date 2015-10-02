from django.shortcuts import render
#from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets, filters
from rest_framework.renderers import BrowsableAPIRenderer, JSONPRenderer,JSONRenderer,XMLRenderer,YAMLRenderer #, filters
#from renderer import CustomBrowsableAPIRenderer
from filters import ReadersFilter,ReaderLocationFilter, TagReadsFilter
from etag.models import Readers, Animal, ReaderLocation,Tags,TagReads,AccessoryData
from serializer import ReaderSerializer, AnimalSerializer
from rest_framework import permissions
#import DjangoModelPermissionsOrAnonReadOnly

class ReadersViewSet(viewsets.ModelViewSet):
    """
    RFID Readers table view set.
    """
    model = Readers
    queryset = Readers.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ReaderSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter) #,filters.OrderingFilter)
    filter_class = ReadersFilter
    search_fields = ('name', 'description',)
    #ordering_fields = ('name', 'description', 'latitude', 'longitude', 'source_no','source__cource')

class ReaderLocationViewSet(viewsets.ModelViewSet):
    """
    Reader Location table view set.
    """
    model = ReaderLocation
    queryset = ReaderLocation.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ReaderLocationSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter) #,filters.OrderingFilter)
    filter_class = ReaderLocationFilter
    search_fields = ('name', 'latitude','longitude','start_date','end_date')
    #ordering_fields = ('name', 'description', 'latitude', 'longitude', 'source_no','source__cource')

class AnimalViewSet(viewsets.ModelViewSet):
    """
    Animal table view set.
    """
    model = Animal
    queryset = Animal.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = AnimalSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    #filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter) #,filters.OrderingFilter)
    #filter_class = ReadersFilter
    search_fields = ('field_data',)
    #ordering_fields = ('name', 'description', 'latitude', 'longitude', 'source_no','source__cource')

class TagsViewSet(viewsets.ModelViewSet):
    """
    Tags table view set.
    """
    model = Tags
    queryset = Tags.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = TagsSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter) #,filters.OrderingFilter)
    filter_class = TagsFilter
    search_fields = ('tag_id',)
    #ordering_fields = ('name', 'description', 'latitude', 'longitude', 'source_no','source__cource')
class TagReadsViewSet(viewsets.ModelViewSet):
    """
    TagReads table view set.
    """
    model = TagReads
    queryset = TagReads.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = TagReadsSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter) #,filters.OrderingFilter)
    filter_class = TagReadsFilter
    search_fields = ('tag_id',)
    #ordering_fields = ('name', 'description', 'latitude', 'longitude', 'source_no','source__cource')
class AccessoryDataViewSet(viewsets.ModelViewSet):
    """
    AccessoryData table view set.
    """
    model =AccessoryData
    queryset = AccessoryData.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    search_fields = ('timestamp','accessory_type','value')
