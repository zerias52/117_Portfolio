from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import projects_list

urlpatterns = [
    path('', projects_list, name='projects_list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)