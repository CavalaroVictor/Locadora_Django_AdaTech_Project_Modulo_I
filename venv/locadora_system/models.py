from django.db import models


class Categoria(models.Model):
    categoria = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.categoria


class Aluguel(models.Model): 
    filme = models.CharField(max_length=200)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=200)
    ano_lancamento = models.DecimalField(max_digits=4, decimal_places=0)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    disponivel = models.BooleanField(null=True)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Alugueis'

    def __str__(self):
        return self.filme