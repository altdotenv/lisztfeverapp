from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from django.urls import include, path  #django 2.0 version url dispatcher
from django.http import HttpResponse
from rest_framework_jwt.views import obtain_jwt_token
from lisztfeverapp import views
import urllib

urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('user/', include("lisztfeverapp.users.urls")),
    path('artist/', include("lisztfeverapp.artists.urls")),
    path('event/', include("lisztfeverapp.events.urls")),
    path('accounts/', include('allauth.urls')),
    path('robots.txt', lambda r: HttpResponse("User-agent: *\nDisallow: /admin/\nSitemap: https://lisztfever.com/sitemap.xml", content_type="text/plain")),
    path('sitemap.xml', lambda r: HttpResponse(urllib.request.urlopen("https://s3.amazonaws.com/lisztfeverapp/sitemap.xml").read(), content_type='text/xml'))
    # Your stuff: custom urls includes go here

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'^', views.ReactAppView.as_view()),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(
            r"^400/$",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        url(
            r"^403/$",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        url(
            r"^404/$",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        url(r"^500/$", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [url(r"^__debug__/", include(debug_toolbar.urls))] + urlpatterns
