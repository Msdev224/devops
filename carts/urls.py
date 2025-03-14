from django.urls import path 


from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove_cart/<int:product_id>/', views.remove_cart, name='remove_cart'),
    path('remove_cart_item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
    # path('checkout/', views.checkout, name='checkout'),
    # path('order/', views.order, name='order'),
    # path('update_cart_item/', views.update_cart_item, name='update_cart_item'),
    # path('order_complete/', views.order_complete, name='order_complete'),
    # path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),
    # path('search/', views.search, name='search'),
    # path('search_auto/', views.search_auto, name='search_auto'),
    # path('order_history/', views.order_history, name='order_history'),
    # path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),
    # path('order_pdf/<int:order_id>/', views.order_pdf, name='order_pdf'),
    # path('order_cancel/<int:order_id>/', views.order_cancel, name='order_cancel'),
    # path('order_return/<int:order_id>/', views.order_return, name='order_return'),
    # path('order_return_pdf/<int:order_id>/', views.order_return_pdf, name='order_return_pdf'),
    # path('order_return_cancel/<int:order_id>/', views.order_return_cancel, name='order_return_cancel'),
    # path('order_return_detail/<int:order_id>/', views.order_return_detail, name='order_return_detail'),
    # path('order_return_history/', views.order_return_history, name='order_return_history'),
    # path('order_return_pdf/<int:order_id>/', views.order_return_pdf, name='order_return_pdf'),
    # path('order_return_cancel/<int:order_id>/', views.order_return_cancel, name='order_return_cancel'),
    # path('order_return_detail/<int:order_id>/', views.order_return_detail, name='order_return_detail'),
]