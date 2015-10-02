__author__ = 'mstacy'
import django_filters

from models import Readers, ReaderLocation,Tags, TagReads

class ReadersFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_type='icontains')
    description = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
        model = Readers
        fields = ['name', 'description',]

class ReaderLocationFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_type='icontains')
    min_lat = django_filters.NumberFilter(name='latitude',lookup_type='gte')
    max_lat = django_filters.NumberFilter(name='latitude',lookup_type='lte')
    min_long = django_filters.NumberFilter(name='longitude',lookup_type='gte')
    max_long = django_filters.NumberFilter(name='longitude',lookup_type='lte')
    min_date = django_filters.DateFilter(name='start_date', lookup_type='gte')
    max_date = django_filters.DateFilter(name='end_date', lookup_type='lte')
    class Meta:
        model = ReaderLocation
        fields = ['name', 'latitude','longitude','start_date','end_date']

class TagsFilter(django_filters.FilterSet):
    tag_id = django_filters.CharFilter(lookup_type='icontains')
    min_date = django_filters.DateFilter(name='start_date', lookup_type='gte')
    max_date = django_filters.DateFilter(name='end_date', lookup_type='lte')
    class Meta:
        model = Tags
        fields = ['name', 'latitude','longitude','start_date','end_date']

class TagReadsFilter(django_filters.FilterSet):
    tag_id = django_filters.CharFilter(lookup_type='icontains')
    min_timestamp = django_filters.DateFilter(name='timestamp', lookup_type='gte')
    max_timestamp = django_filters.DateFilter(name='timestamp', lookup_type='lte')
    class Meta:
        model = TagReads
        fields = ['tag_id',]
