from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('arts/',views.gallery,name='gallery'),
    path('photo/<str:pk>/',views.viewPhoto,name='photo'),
    path('add/',views.addPhoto,name='add'),
    path('login/',views.loginpage,name='login'),
    path('section/',views.section),
    path('verify/<auth_token>',views.verify,name='verify'),
    path('exit/',views.exit,name='exit')

]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)   #to fetch image from static/images
urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 