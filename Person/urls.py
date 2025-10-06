from django.urls import path
from .views import register, acceuil
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy

urlpatterns = [
    path('register/', register, name="Reg"),
    path('Acceuil/', acceuil, name="Acc"),
    path('login/', LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name="Login"),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('Acc')), name="LogO"),
]
