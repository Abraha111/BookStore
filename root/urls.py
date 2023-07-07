
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf.urls.static import static
from root.settings import STATIC_ROOT, STATIC_URL, MEDIA_URL, MEDIA_ROOT


schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version="v1",
        description="API documentation",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],

)

urlpatterns = [
        path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

        path('admin/', admin.site.urls),
        path('api/', include('api.urls'))
] + static(STATIC_URL, document_root=STATIC_ROOT) + static(MEDIA_URL, document_root=MEDIA_ROOT)
