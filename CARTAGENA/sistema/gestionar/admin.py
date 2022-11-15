from django.contrib import admin
from .models import matriculaEscolar
from .models import fuerzaTrabajo
from .models import desempleo
from .models import pobrezaMonetaria
from .models import pobrezaExtrema
from .models import matriculanivelEducatico
from .models import homicidios
from .models import accidentes
from .models import suicidios
from .models import atropellos
from .models import comparendos


# Register your models here.
admin.site.register(matriculaEscolar)
admin.site.register(fuerzaTrabajo)
admin.site.register(desempleo)
admin.site.register(pobrezaMonetaria)
admin.site.register(pobrezaExtrema)
admin.site.register(matriculanivelEducatico)
admin.site.register(homicidios)
admin.site.register(accidentes)
admin.site.register(suicidios)
admin.site.register(atropellos)
admin.site.register(comparendos)




