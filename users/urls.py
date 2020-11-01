from django.urls import path
from django.conf.urls.static import static
from shopex import settings

app_name = 'users'
urlpatterns = [

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
