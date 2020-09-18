from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import product_detail, product_list


app_name = 'shop'


urlpatterns = [
    path('', product_list, name='product_list'),
    path('/<int:id>/<slug:slug>/', product_detail, name='product_detail'),
    path('<slug:category_slug>/', product_list, name='product_list_by_category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
