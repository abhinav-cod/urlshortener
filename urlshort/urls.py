from django.urls import path

from .views import index,redirect_view
appname='urlshort'


urlpatterns=[
    path("",index,name='home'),
    path("<str:tiny_path>",redirect_view,name='redirect'),
]
