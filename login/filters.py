import django_filters
from django_filters import DateFilter

from .models import *


class rechargeFilter(django_filters.FilterSet):
    start_date=DateFilter(field_name="date",lookup_expr='gte')
    end_date=DateFilter(field_name="date",lookup_expr='lte')
    class Meta:
        model=recharge 
        fields = '__all__'
        exclude=['uname','fname','s_provider','status','commision','category','service_no','date']