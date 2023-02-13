from django.forms import ModelForm
from .models import Aluguel


class AluguelForm(ModelForm):
    class Meta:
        model = Aluguel
        fields = ['filme', 'descricao', 'ano_lancamento', 'valor', 'categoria', 'disponivel', 'observacoes']