import django_filters
from .models import Tvshow

class TvshowFilter(django_filters.FilterSet):
    class Meta:
        model = Tvshow
        fields =['language','category','channel','release_year']