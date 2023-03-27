from django.urls import path, include
from Inicio import views
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static

urlpatterns = [
    path('',views.refe, name="Inicio"),
    path('Inicio/',login_required(views.Inicio), name="dona"),
    path('Grac/',views.Gra, name="Gracias"),
    path('Eli/',views.Elim, name="Eliminado"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)