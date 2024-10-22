from django import forms
from .models import Libro
from .models import Usuario


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields= '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre_usuario',
            'nombre',
            'apellidos',
            'email',
            'edad',
            'peso',
            'altura',
            'fecha_nacimiento',
            'roles',
             ]