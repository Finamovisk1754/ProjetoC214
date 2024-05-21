
from django.contrib import admin
from django.urls import path, include, router


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('projects.urls')),
]

urlpatterns = [
    path('', include(router.urls)),
]