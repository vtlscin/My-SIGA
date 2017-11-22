from django.shortcuts import render
from .models import Prova
from .models import Turma
from .models import Aluno
from .models import Professor
from .models import Escola
from django.utils import timezone

def menu(request):
	allnota = Prova.objects.all()	
	return render(request, 'siga/menu.html', {'allnota': allnota})
