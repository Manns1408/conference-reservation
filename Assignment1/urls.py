from django.urls import path, include
from django.contrib import admin
from reservations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
    path('register/', views.registering, name='register'),
    path('rooms/', views.room_lists, name='room_list'),
    path('rooms/<int:pk>/', views.room_detail, name='room_detail'),
    path('myReservations/', views.my_reservations, name='my_reservations'),
    path('edit/<int:pk>/', views.reservation_editing, name='reservation_edit'),
    path('cancel/<int:pk>/', views.reservations_cancelling, name='reservation_cancel'),
    path('status/', views.room_status, name='room_status'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('send-test-email/', views.test_email, name='test_email'),

]
