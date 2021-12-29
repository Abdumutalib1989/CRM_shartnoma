from django.contrib import admin
from django.urls import path
from tolov.views import TolovListCreateAPIView, TolovGetUpdateAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tolov/', TolovListCreateAPIView.as_view(), name="tolovlar"),
    path('tolov/<int:pk>', TolovGetUpdateAPIView.as_view()),
]
