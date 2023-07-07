from django.urls import path
import views
urlpatterns = [
    
path( 'booking/' , views.bookingview.as_view()),
path('items/', views.MenuItemsView.as_view()),
path('items/<int:pk>', views.SingleMenuItemView.as_view()),

]