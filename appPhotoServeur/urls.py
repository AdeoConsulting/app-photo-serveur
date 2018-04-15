from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^api/', include('photo.urls')), # C'est ici que nous ajouttons l'urls de l'app photo
]

# tres important pour pouvoir afficher les photos telecharger dans notre navigateur
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)