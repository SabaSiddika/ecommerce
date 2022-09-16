from django.urls import path
from shop import views
urlpatterns = [
    path('',views.index,name='ShopHome'),
    path('about/',views.about,name='AboutUs'),
    path('contact/',views.contact,name='Contact Us'),
    path('tracker/',views.tracker,name='Tracking Status'),
    path('search/',views.search,name='Search'),
    path('products/<int:id>',views.productview,name='ProductView'),
    path('checkout/',views.checkout,name='checkout'),
]
