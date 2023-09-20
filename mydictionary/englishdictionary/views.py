from django.shortcuts import render
# from PyDictionary import PyDictionary
from PyMultiDictionary import MultiDictionary
# Create your views here.

def base(request):
    "Репрезентация начальной страницы словаря"
    return render(request, 'base.html')

def word_info(request):
    "Репрезентация страницы с информацией по искомому слову"
    dictionary = MultiDictionary()
    if request.method == 'POST':
        word = request.POST['word']
        meaning = dictionary.meaning('en', word)
        antonyms = dictionary.antonym('en', word)
        synonyms = dictionary.synonym('en', word)
        translation = dictionary.translate('en', word, to='ru')

        return render(request, 'word_info.html', 
                      {'word': word, 
                        'meaning': meaning, 
                        'antonyms': antonyms, 
                        'synonyms': synonyms,
                        'translation': translation }
                       )
    
    return render(request, 'word_info.html')