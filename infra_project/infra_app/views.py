from django.http import HttpResponse

html_code = """<img src="https://warfiles.ru/uploads/
posts/2018-03/1521565606_1468661375_1.jpg"
height="300px" />"""


def index(request):
    return HttpResponse(html_code)


def second_page(request):
    return HttpResponse('А это вторая страница')
