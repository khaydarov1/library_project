from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Book list Api",
        default_version='v1',
        description="Library demo project",
        terms_of_service="gemo.com",
        contact=openapi.Contact(email="jhaydarov2002@gmail.com"),
        license=openapi.License(name="demo license")
    ),
    public=True,
    # permissions_classes=[permissions.AllowAny, ],

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('books.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/book/rest-auth/', include('dj_rest_auth.urls')),
    path('api/book/rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    # swegger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema_redoc')
]
