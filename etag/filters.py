__author__ = 'mstacy'
import django_filters

from models import Readers

class ReadersFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_type='icontains')
    description = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
        model = Readers
        fields = ['name', 'description',]
