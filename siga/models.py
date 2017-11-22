from django.db import models
from django.utils import timezone 


class Prova(models.Model):
	materia = models.CharField(max_length = 20)
	unidade = models.CharField(max_length = 10)
	data = models.DateTimeField(default = timezone.now)
	valor = models.DecimalField(max_digits = 4, decimal_places = 2)
	def __str__(self):
		return self.materia
	
		


class Turma(models.Model):
	nome = models.CharField(max_length=30)
	data_criacao = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.nome


class Aluno(models.Model):
	turma = models.ForeignKey(Turma)
	nome = models.CharField(max_length = 20)
	responsavel = models.CharField(max_length = 20)
	nascimento = models.DateTimeField(default = timezone.now)
	prova = models.ManyToManyField(Prova)

	def __str__(self):
		return self.nome

class Professor(models.Model):
	turma = models.ManyToManyField(Turma)
	nome = models.CharField(max_length = 20)
	disciplina = models.CharField(max_length = 30)

	def __str__(self):
		return self.nome

class Escola(models.Model):
	nome = models.CharField(max_length = 20)
	professor = models.ForeignKey(Professor)
	aluno = models.ForeignKey(Aluno)
	
	def __str__(self):
		return self.nome	


