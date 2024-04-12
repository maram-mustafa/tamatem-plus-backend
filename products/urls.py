from django.urls import path

from products.views import ProductDetailsEditView, ProductListView

urlpatterns = [
    path("products", ProductListView.as_view(), name="product_list"),
    path(
        "products/<int:pk>/",
        ProductDetailsEditView.as_view(),
        name="product_detail_edit",
    ),
]
