"""
URL configuration for mysite project.

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
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from app.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap
from blog.feeds import LatestEntriesFeed
# ======================================================================================================================
sitemaps = {
    "static": StaticViewSitemap,
    "blog": BlogSitemap,
}
# ======================================================================================================================
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('', include('blog.urls')),
    path('accounts/', include('account.urls')),
    path(
        "sitemap.xml/",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path('robots.txt/', include('robots.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path("rss/feed/", LatestEntriesFeed()),
    path('captcha/', include('captcha.urls')),

]
# ======================================================================================================================
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
