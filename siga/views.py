from django.shortcuts import render

def menu(request):
    return render(request, 'siga/menu.html', {})
