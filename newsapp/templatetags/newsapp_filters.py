from django import template

register = template.Library()


stop_words = ['запрещенные слова', 'мат', 'ругательства'] # Список запрещенных слов


@register.filter(name='censor')
def censor(value):
    text = value.split()
    for word in text:
        if word.lower() in stop_words:
            value = value.replace(word, '****')
    return value