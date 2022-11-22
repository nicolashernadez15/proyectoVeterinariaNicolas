from django import forms
from django.forms import ModelForm
from .models import Mascota, ConsultaMedica, estetica, vacuna, cirugia,dueño

class MascotaForm(forms.Form):
    nombre = forms.ModelChoiceField(queryset=Mascota.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    dueño = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    edad = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    descripcion = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 4:
            raise forms.ValidationError("El nombre debe tener al menos 4 caracteres")
        return nombre

class MascotaForm(ModelForm):
    class Meta:
        model = Mascota
        fields ='__all__'

        nombre = forms.ModelChoiceField(queryset=Mascota.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
        dueño = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
        edad = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
        descrpcion = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 4:
            raise forms.ValidationError("El nombre debe tener al menos 4 caracteres")
        return nombre

class consultaForm(forms.Form):
    nombre = forms.ModelChoiceField(queryset=Mascota.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    fecha = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    motivo = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    diagnostico = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    tratamiento = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    observaciones = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    valor = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 4:
            raise forms.ValidationError("El nombre debe tener al menos 4 caracteres")


class consultaForm(ModelForm):
    nombre = forms.ModelChoiceField(queryset=Mascota.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    fecha = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    motivo = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    diagnostico = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    tratamiento = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    observaciones = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    valor = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))


class consultaForm(ModelForm):
    class Meta:
        model = ConsultaMedica
        fields ='__all__'

class esteticaForm(forms.Form):
    nombre = forms.ModelChoiceField(queryset=Mascota.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    fecha = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    motivo = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    diagnostico = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    tratamiento = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    observaciones = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    valor = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 4:
            raise forms.ValidationError("El nombre debe tener al menos 4 caracteres")

class esteticaForm(ModelForm):
    nombre = forms.ModelChoiceField(queryset=Mascota.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    fecha = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    motivo = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    diagnostico = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    tratamiento = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    observaciones = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    valor = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))


class esteticaForm(ModelForm):
    class Meta:
        model = estetica
        fields ='__all__'

class vacunaForm(forms.Form):
    nombre = forms.ModelChoiceField(queryset=Mascota.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    fecha = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    motivo = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    diagnostico = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    tratamiento = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    observaciones = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    valor = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 4:
            raise forms.ValidationError("El nombre debe tener al menos 4 caracteres")


class vacunaForm(ModelForm):
    nombre = forms.ModelChoiceField(queryset=Mascota.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    fecha = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    motivo = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    diagnostico = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    tratamiento = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    observaciones = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    valor = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))


class vacunaForm(ModelForm):
    class Meta:
        model = vacuna
        fields ='__all__'

class cirugiaForm(forms.Form):
    nombre = forms.ModelChoiceField(queryset=Mascota.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    fecha = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    motivo = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    diagnostico = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    tratamiento = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    observaciones = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    valor = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 4:
            raise forms.ValidationError("El nombre debe tener al menos 4 caracteres")


class cirugiaForm(ModelForm):
    nombre = forms.ModelChoiceField(queryset=Mascota.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    fecha = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    motivo = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    diagnostico = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    tratamiento = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    observaciones = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    valor = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))


class cirugiaForm(ModelForm):
    class Meta:
        model = cirugia
        fields ='__all__'


class dueñoForm(forms.Form):
    dueño = forms.ModelChoiceField(queryset=dueño.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    apellido = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    edad = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    sexo = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 4:
            raise forms.ValidationError("El nombre debe tener al menos 4 caracteres")


class dueñoForm(ModelForm):
    dueño = forms.ModelChoiceField(queryset=dueño.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    apellido = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    edad = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    sexo = forms.CharField(label="Nombre de categoria", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    

class dueñoForm(ModelForm):
    class Meta:
        model = dueño
        fields ='__all__'