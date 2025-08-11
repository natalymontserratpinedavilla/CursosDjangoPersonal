from django.contrib import admin
from .models import Actividad
from .models import Cursos

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'precio', 'duracion_horas')  
    search_fields = ('nombre', 'descripcion')
    date_hierarchy = ('created')
    list_filter = ('duracion_horas','nombre')   


admin.site.register(Cursos, AdministrarModelo)


class AdministrarActividad(admin.ModelAdmin):
    list_display = ('id', 'actividad', 'coment', 'created')  # Mostrar también la FK y la fecha
    search_fields = ('id', 'coment')  # 'created' no es buena opción para búsqueda por texto
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
    list_filter = ('actividad', 'created')  # Filtro útil por actividad o fecha

admin.site.register(Actividad, AdministrarActividad)