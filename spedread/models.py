from django.db import models


#INÍCIO DO DETALHAMENTO DO GUIA 
class Bloco(models.Model):
	nome = models.CharField(max_length=255)
	descricao = models.CharField(max_length=255)

	def __str__(self):
		return 'Bloco '+self.nome

class Registro(models.Model):
	bloco = models.ForeignKey(Bloco)
	nome = models.CharField(max_length=255)
	descricao = models.CharField(max_length=255)


	def __str__(self):
		return self.nome

class Campo(models.Model):
	registro = models.ForeignKey(Registro)
	num_posicao = models.IntegerField()
	nome = models.CharField(max_length=255)
	descricao = models.CharField(max_length=255)

	def __str__(self):
		return self.nome

class ValoresPadroes():
	campo = models.ForeignKey(Campo)
	valor = models.CharField(max_length=255)
	descricao = models.CharField(max_length=255)

#FIM DO DETALHAMENTO

#INÍCIO DA LEITURA DE DADOS DO DOCUMENTO

class Sped(models.Model):
	data_upload =  models.DateField()
	nome = models.CharField(max_length=255)

class ValoresSped(models.Model):
	sped = models.ForeignKey(Sped)
	campo = models.ForeignKey(Campo)
	valor = models.CharField(max_length=255)
	fim_linha = models.BooleanField()

#FIM DA LEITURA DE DADOS DO DOCUMENTO