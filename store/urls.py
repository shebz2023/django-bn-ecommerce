from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path("products/", views.product_list),
    path("products/<int:id>/", views.singleProduct),
    path("collection/<int:pk>/", views.collection_details, name="collection-details"),
]
