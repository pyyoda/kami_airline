from config import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path

# Redirects an invalid/empty path url to Admin View
from django.views.generic.base import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        RedirectView.as_view(url="/admin/", permanent=False),
        name="empty-path-redirect",
    ),
    path("airplanes/", include(("airplane.urls", "airplane"), namespace="airplane")),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
