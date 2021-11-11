from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import NewsModel
from datetime import datetime
from .filters import NewsFilter
from .forms import NewsForm



class NewsViews(ListView):
    model = NewsModel
    template_name = 'flatpages/news.html'
    context_object_name = 'news'
    queryset = NewsModel.objects.order_by('-dateCreation')
    paginate_by = 1
    form_class = NewsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        context['form'] = NewsForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)


class NewsSearch(ListView):
    model = NewsModel
    template_name = 'flatpages/news_search.html'
    context_object_name = 'search'
    queryset = NewsModel.objects.order_by('-dateCreation')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET,
                                          queryset=self.get_queryset())
        return context

class Post(DetailView):
    model = NewsModel
    template_name = 'flatpages\post.html'
    context_object_name = 'post'


# дженерик для редактирования объекта
class NewsUpdateView(UpdateView):
    template_name = 'flatpages/news_update.html'
    form_class = NewsForm
    context_object_name = 'update'

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return NewsModel.objects.get(pk=id)


# дженерик для удаления товара
class NewsDeleteView(DeleteView):
    template_name = 'flatpages/news_delete.html'
    queryset = NewsModel.objects.all()
    success_url = '/news/'
    context_object_name = 'news_delete'

# дженерик для получения деталей о товаре
class NewsDetailView(DetailView):
    template_name = 'flatpages/news_detail.html'
    queryset = NewsModel.objects.all()
    context_object_name = 'news_detail'

# дженерик для создания объекта. Надо указать только имя шаблона и класс формы, который мы написали в прошлом юните. Остальное он сделает за вас
class NewsCreateView(CreateView):
    template_name = 'flatpages/news_create.html'
    form_class = NewsForm
    context_object_name = 'news_create'
