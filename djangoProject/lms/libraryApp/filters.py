import django_filters

from .models import *

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = BOOK
        fields = ['bookTitle']
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                    'label' :""
                },
            },
        }
