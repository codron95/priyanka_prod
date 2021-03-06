"""priyanka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from . import settings
from django.conf.urls.static import static
from index import views
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index ),
    url(r'scrible/(?P<type>\w+)/(?P<link>[-\w]+)/',views.scrible, name="scrible-param"),
    url(r'scrible/(?P<type>\w+)/',views.scrible),
    url(r'clicks/(?P<type>\w+)/',views.clicks),
    url(r'^subscribe/$',views.subscribe),
    url(r'^contact/$',views.contact),
    url(r'^search/$',views.search),
    url(r'^fetch/$',views.return_comments),
    url(r'^create/$',views.create_comment),
    url(r'^test/$',views.test),
    url(r'^fetch/$',views.return_comments),
    url(r'^create/$',views.create_comment),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
