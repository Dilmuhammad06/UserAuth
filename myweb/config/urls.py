from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

app_name = 'userauth'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('student.urls')),
    path('auth/', include(('userauth.urls', app_name), namespace='users')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
