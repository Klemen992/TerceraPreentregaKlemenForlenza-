
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplicacion.urls'))        #'' osea nada, porque tenes una sola aplicacion
]

#''Signficia que cuando no pones nada en la web como ruta, te aparece esto como pagina standard