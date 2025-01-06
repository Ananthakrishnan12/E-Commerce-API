from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('product/',ProductListView.as_view()),
    path('product/<int:id>',ProductDetailView.as_view()),
    path('order/',OrderCreateView.as_view()),
    path('order/list/',OrderListView.as_view()),
    path('order/<int:order_id>/cancel/',OrderCancelView.as_view()),
    path('payment/<int:order_id>/', MockPaymentView.as_view())
]