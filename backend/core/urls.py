"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls.i18n import i18n_patterns # Wrap whole urls patterns to add translation to all urls
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views import set_language

urlpatterns = [
    path('api/v1/account/', include('account.v1.urls', namespace='v1-account')),
    path('api/v1/call/', include('call.v1.urls', namespace='v1-call')),
    path('admin/', admin.site.urls),

]

urlpatterns += [
    path("setlang/", set_language, name="set_language"),
    path('api-auth/', include('rest_framework.urls')),
    # re_path(r'^rosetta/', include('rosetta.urls')),
    # path('hijack/', include('hijack.urls')),
    # path("ckeditor5/", include('django_ckeditor_5.urls')),

    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path(
        'api/schema/docs/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='documentation'
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
