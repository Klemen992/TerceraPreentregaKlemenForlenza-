from django.urls import path, include
from .views import*

urlpatterns = [
    path('',home, name="home"),
    path('plants/',plantas, name="pflanzen"),
    path('flowerpot/',macetas, name="blumentoepfe"),
    path('gardering/',jardineria, name="garten"),
    path('decoration/',decoracion, name="dekoration"),

    path('plantsForm/',plantasForm, name="plantas_form"),
    path('plantsForm2/',plantasForm2, name="plantas_form2"),

    path('searchSpecies/',buscarEspecie, name="suchen_gattung"),
    path('search2/',buscar2, name="suchen_2"),

]

#'': Es la ruta
#home: es la def