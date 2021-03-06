from django.urls import path

from .views import image_create, image_detail, image_like, image_ranking, image_list


app_name = 'images'


urlpatterns = [
    path('create/', image_create, name='image_create'),
    path('detail/<int:id><slug:slug>', image_detail, name='image_detail'),
    path('like/', image_like, name='like'),
    path('ranking/', image_ranking, name='image_ranking'),
    path('list/', image_list, name='image_list')
]
