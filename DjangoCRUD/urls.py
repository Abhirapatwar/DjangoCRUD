from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_data, name='index'),
    path('delete/<int:id>/', views.delete_data, name='deletedata'),
    path('update/<int:id>/', views.update_data, name='updatedata'),
]
