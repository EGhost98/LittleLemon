from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from reservation import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('reservation.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('restaurant/booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]
