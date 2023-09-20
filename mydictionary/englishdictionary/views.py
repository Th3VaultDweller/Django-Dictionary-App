from django.shortcuts import render
from PyDictionary import PyDictionary
# Create your views here.

def base(request):
    "Репрезентация начальной страницы словаря"
    return render(request, 'base.html')

def word_info(request):
    "Репрезентация страницы с информацией по искомому слову"
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    synonyms = dictionary.synonym(search)
    antonyms = dictionary.antonym(search)

    context = {
        'meaning': meaning, 
        'synonyms': synonyms,
        'antonyms': antonyms
    }

    return render(request, 'word_info.html', context)