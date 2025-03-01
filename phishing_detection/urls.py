from django.urls import path,include
from .views import some_view  # Replace with actual views
 from django.contrib import admin


urlpatterns = [
    path('test/', some_view, name='test'),  # Example route
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Ensures `core/urls.py` is included
    path('', include('automated.urls')),  # Ensures `automated/urls.py` is included
    path('api/secure/', secure_view, name='secure_view'),
]
