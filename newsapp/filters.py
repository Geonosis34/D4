from django_filters import FilterSet
from .models import NewsModel


# создаём фильтр
class NewsFilter(FilterSet):
    class Meta:
        model = NewsModel
        fields = {'name':['icontains'],
        'description':['icontains'],
        'author':['icontains'],
        'dateCreation':['gte'],
        'id':['exact'],
                  }