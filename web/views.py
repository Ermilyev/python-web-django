from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

publication_date = [
    {
        'id': 0,
        'title': 'Что такое Lorem Ipsum?',
        'date': datetime.now(),
        'text': 'Lorem Ipsum - это текст-"рыба", часто используемый в печати и вэб-дизайне. Lorem Ipsum является '
                'стандартной рыбой для текстов на латинице с начала XVI века. В то время некий безымянный печатник '
                'создал большую коллекцию размеров и форм шрифтов, используя Lorem Ipsum для распечатки образцов. '
                'Lorem Ipsum не только успешно пережил без заметных изменений пять веков, но и перешагнул в '
                'электронный дизайн. Его популяризации в новое время послужили публикация листов Letraset с образцами '
                'Lorem Ipsum в 60-х годах и, в более недавнее время,программы электронной вёрстки типа Aldus '
                'PageMaker, в шаблонах которых используется Lorem Ipsum. '
    },
    {
        'id': 1,
        'title': 'Почему он используется?',
        'date': datetime.now(),
        'text': 'Давно выяснено, что при оценке дизайна и композиции читаемый текст мешает сосредоточиться. Lorem '
                'Ipsum используют потому, что тот обеспечивает более или менее стандартное заполнение шаблона, '
                'а также реальное распределение букв и пробелов в абзацах, которое не получается при простой '
                'дубликации "Здесь ваш текст.. Здесь ваш текст.. Здесь ваш текст.." Многие программы электронной '
                'вёрстки и редакторы HTML используют Lorem Ipsum в качестве текста по умолчанию, так что поиск по '
                'ключевым словам "lorem ipsum" сразу показывает, как много веб-страниц всё ещё дожидаются своего '
                'настоящего рождения. За прошедшие годы текст Lorem Ipsum получил много версий. Некоторые версии '
                'появились по ошибке, некоторые - намеренно (например, юмористические варианты). '
    },
    {
        'id': 2,
        'title': 'Откуда он появился?',
        'date': datetime.now(),
        'text': 'Многие думают, что Lorem Ipsum - взятый с потолка псевдо-латинский набор слов, но это не совсем так. '
                'Его корни уходят в один фрагмент классической латыни 45 года н.э., то есть более двух тысячелетий '
                'назад. Ричард МакКлинток, профессор латыни из колледжа Hampden-Sydney, штат Вирджиния, взял одно из '
                'самых странных слов в Lorem Ipsum, "consectetur", и занялся его поисками в классической латинской '
                'литературе. В результате он нашёл неоспоримый первоисточник Lorem Ipsum в разделах 1.10.32 и 1.10.33 '
                'книги "de Finibus Bonorum et Malorum" ("О пределах добра и зла"), написанной Цицероном в 45 году '
                'н.э. Этот трактат по теории этики был очень популярен в эпоху Возрождения. Первая строка Lorem '
                'Ipsum, "Lorem ipsum dolor sit amet..", происходит от одной из строк в разделе 1.10.32 Классический '
                'текст Lorem Ipsum, используемый с XVI века, приведён ниже. Также даны разделы 1.10.32 и 1.10.33 "de '
                'Finibus Bonorum et Malorum" Цицерона и их английский перевод, сделанный H. Rackham, 1914 год. '
    },
    {
        'id': 3,
        'title': 'Где его взять?',
        'date': datetime.now(),
        'text': 'Есть много вариантов Lorem Ipsum, но большинство из них имеет не всегда приемлемые модификации, '
                'например, юмористические вставки или слова, которые даже отдалённо не напоминают латынь. Если вам '
                'нужен Lorem Ipsum для серьёзного проекта, вы наверняка не хотите какой-нибудь шутки, '
                'скрытой в середине абзаца. Также все другие известные генераторы Lorem Ipsum используют один и тот '
                'же текст, который они просто повторяют, пока не достигнут нужный объём. Это делает предлагаемый '
                'здесь генератор единственным настоящим Lorem Ipsum генератором. Он использует словарь из более чем '
                '200 латинских слов, а также набор моделей предложений. В результате сгенерированный Lorem Ipsum '
                'выглядит правдоподобно, не имеет повторяющихся абзацей или "невозможных" слов. '
    }
]


def index(request):
    return render(request, 'main.html')


def contacts(request):
    return render(request, 'contacts.html')


def post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        text = request.POST.get('text')
        if title and text:
            publication_date.append({
                'id': len(publication_date),
                'title': title,
                'date': datetime.now(),
                'text': text
            })
            return redirect('/publications')
        else:
            return render(request, 'post.html', {
                'error': 'title и text должны быть не пустыми'
            })
    return render(request, 'post.html')


def publications(request):
    publication_sorted = sorted(publication_date,
                                     key=lambda pub: pub['date'],
                                     reverse=True)
    return render(request, 'publications.html', {
        'publications': publication_sorted
    })


def publication(request, pub_id):
    if pub_id >= len(publication_date):
        return redirect('/')
    return render(request, 'publication.html', publication_date[pub_id])


def status(request):
    return HttpResponse("Status OK")
