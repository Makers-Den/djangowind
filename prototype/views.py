from django.shortcuts import render

# Create your views here.


def index(request):
    rows = [{'title': 'first'}, {'title': 'second'}, {'title': 'third'}]
    cards = [
        {'title': 'Card1', 'img': 'http://lorempixel.com/400/400/nature/',
            'tags': ['example', 'foobar']},
        {'title': 'Card1', 'img': 'http://lorempixel.com/400/400/animals/',
            'tags': ['tags', 'foobar']}
    ]
    return render(request, 'exampleview.html', {'rows': rows, 'cards': cards})
