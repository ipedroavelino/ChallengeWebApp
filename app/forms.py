from django.forms import ModelForm, fields
from app.models import Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha', 'telefone']