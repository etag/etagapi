from django.shortcuts import render
#from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets, filters, status
from rest_framework.renderers import BrowsableAPIRenderer, JSONPRenderer,JSONRenderer,XMLRenderer,YAMLRenderer #, filters
from rest_framework.parsers import JSONParser
#from renderer import CustomBrowsableAPIRenderer
from filters import ReadersFilter,ReaderLocationFilter, TagReadsFilter,TagsFilter, AnimalFilter
from etag.models import Readers, TagAnimal, ReaderLocation,Tags,TagReads,AccessoryData
from serializer import ReaderSerializer, AnimalSerializer,ReaderLocationSerializer,TagsSerializer,TagReadsSerializer
from rest_framework import permissions
from rest_framework.response import Response
#import DjangoModelPermissionsOrAnonReadOnly


class ReadersViewSet(viewsets.ModelViewSet):
    """
    RFID Readers table view set.
    """
    model = Readers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ReaderSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    filter_class = ReadersFilter
    search_fields = ('name', 'description',)
    ordering_fields =  '__all__'
    ordering_fields = '__all__'
    
    def get_queryset(self):
        user = self.request.user
        if not user:
            return []	
        return Readers.objects.filter(user_id=user.id)

    def create(self, request):
        serializer = self.serializer_class(data=request.DATA)

        if serializer.is_valid():
            reader = Readers.objects.create(reader_id=serializer.data['reader_id'],name=serializer.data['name'],description=serializer.data['description'])
            reader.user_id = self.request.user.id
            reader.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReaderLocationViewSet(viewsets.ModelViewSet):
    """
    Reader Location table view set.
    """
    model = ReaderLocation
    queryset = ReaderLocation.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ReaderLocationSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    filter_class = ReaderLocationFilter
    search_fields = ('name', 'latitude','longitude','start_timestamp','end_timestamp')
    ordering_fields = '__all__'

	
class AnimalViewSet(viewsets.ModelViewSet):
    """
    Animal table view set.
    """
    model = TagAnimal
    queryset = TagAnimal.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = AnimalSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    filter_class = AnimalFilter
    ordering_fields = ('name', 'description', 'end_timestamp', 'start_timestamp')

	
class TagsViewSet(viewsets.ModelViewSet):
    """
    Tags table view set.
    """
    model = Tags
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = TagsSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter ,filters.OrderingFilter)
    filter_class = TagsFilter
    search_fields = ('tag_id',)
    ordering_fields = '__all__'
	
    def get_queryset(self):
        user = self.request.user
        if not user:
            return []
        return Tags.objects.filter(user_id=user.id)
		
    def create(self, request):
        serializer = self.serializer_class(data=request.DATA)

        if serializer.is_valid():
            reader = Tags.objects.create(tag_id=serializer.data['tag_id'],name=serializer.data['name'],description=serializer.data['description'])
            reader.user_id = self.request.user.id
            reader.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
class TagReadsViewSet(viewsets.ModelViewSet):
    """
    TagReads table view set.
    """
    model = TagReads
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = TagReadsSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = TagReadsFilter
    search_fields = ('tag_id',)
    ordering_fields =  '__all__' 
	
    def get_queryset(self):
        user = self.request.user
        if not user:
            return []
        
    #    queryset = []
    #    for read in TagReads.objects.all():
    #        reltags = Tags.objects.filter(tag_id=read.tag)
    #        if len(reltags) != 1:
    #            continue
    #        elif read.user_id == reltags[0].user_id:
    #           queryset.append(read)
    #    return queryset      
        return TagReads.objects.filter(tag__user_id = user.id)
	
class AccessoryDataViewSet(viewsets.ModelViewSet):
    """
    AccessoryData table view set.
    """
    model=AccessoryData
    queryset = AccessoryData.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, JSONPRenderer, XMLRenderer, YAMLRenderer)
    search_fields = ('accessory_type', 'value')
