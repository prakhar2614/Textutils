from django.contrib import admin
from django.urls import path
from.import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('analyze', views.analyze, name='analyze'),
    path('contactus', views.contactus, name='contactus'),
    path('aboutus', views.aboutus, name='aboutus'),

]
