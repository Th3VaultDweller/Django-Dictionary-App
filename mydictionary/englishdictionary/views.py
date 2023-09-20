from django.shortcuts import render
from PyDictionary import PyDictionary
# Create your views here.

def base(request):
    "Репрезентация начальной страницы словаря"
    return render(request, 'base.html')

def word_info(request):
    "Репрезентация страницы с информацией по искомому слову"
    dictionary = PyDictionary()
    if request.method == 'POST':
        word = request.POST['word']
        meaning = dictionary.meaning(word)
        antonyms = dictionary.antonym(word)
        synonyms = dictionary.synonym(word)

        # context = {
        #     'meaning': meaning['Noun'][0],
        #     'synonym': synonyms,
        #     'antonym': antonyms,
        # }

        return render(request, 'word_info.html', 
                      {'word': word, 
                       'meaning': meaning, 
                       'antonym': antonyms, 
                       'synonym': synonyms }
                       )
    
    return render(request, 'word_info.html')