from django.urls import path
from . import views
app_name='music'
urlpatterns = [
    path('',views.index,name="index"),
    path('<int:album_id>/',views.details, name='details'),
    path('<int:album_id>/favourite/',views.favourite, name='favourite')
]