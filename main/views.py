from django.http import response
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == 'GET':
        return render(request, 'main/index.html')
    elif request.method == 'POST':
        main = request.POST.get('main')
        temp = request.POST.get('temp')
        file = request.FILES['fin']

        file_name = file.name.split('.')[0]
        file_ext = file.name.split('.')[-1]
        txt_content = file.read().decode('utf-8')

        output_content = txt_content.replace(main, temp)

        response = HttpResponse(output_content, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="out-{}.{}"'.format(file_name, file_ext)

        return response
