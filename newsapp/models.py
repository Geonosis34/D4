from django.db import models



class NewsModel(models.Model):
    name = models.CharField(max_length=150,unique=True)
    description = models.TextField()
    author = models.CharField(max_length=50)
    dateCreation = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/news/{self.id}'
