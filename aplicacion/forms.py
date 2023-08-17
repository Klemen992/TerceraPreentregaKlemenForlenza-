from django import forms

class PlantasForm(forms.Form):
    especie = forms.CharField(max_length=50, required=True)
    genero = forms.CharField(max_length=50, required=True)
    precio = forms.IntegerField(required=True)
    TAMANIOS = (
        (1, "Chico"),
        (2, "Medio"),
        (3, "Grande"),
    )
    tamanio = forms.ChoiceField(label="Tamanio elegido", choices=TAMANIOS, required=True)
    fertilizada = forms.BooleanField()

        
    