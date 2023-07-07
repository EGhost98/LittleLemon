from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from reservation import views

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/menu/', include('reservation.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('restaurant/booking/', include(router.urls)),
]
