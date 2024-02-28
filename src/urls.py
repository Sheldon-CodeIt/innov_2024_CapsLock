from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views  import main_home
urlpatterns = [
    path('accounts/', include('accounts.urls')),  # Accounts URLs
    path('admin/', admin.site.urls),
    path('', main_home, name='main_home'),
    path('courses/', include('course.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)