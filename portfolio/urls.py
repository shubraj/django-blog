"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
import debug_toolbar
urlpatterns = [
    path('logmein/', admin.site.urls),
    path("dashboard/",include("dashboard.urls",namespace="dashboard")),
    path("blogs/",include("blog.urls",namespace="blog")),
    path("",include('resume.urls',namespace="resume")),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns+=path("__debug__",include(debug_toolbar.urls)),
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    handler500 = 'portfolio.handlers.server_error'
    handler404 = 'portfolio.handlers.page_not_found'