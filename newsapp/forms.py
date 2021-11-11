from django.forms import ModelForm, BooleanField
from .models import NewsModel


# Создаём модельную форму
class NewsForm(ModelForm):
    check_box = BooleanField(label='Согласен!')
    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = NewsModel
        fields = ['name', 'description', 'author', 'check_box']