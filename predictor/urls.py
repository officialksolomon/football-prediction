from django.urls import path
from . import views


app_name = 'predictor'
urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('predictions/', views.PredictionView.as_view(), name='predictions'),
    # path('<int:question_id>/', views.detail, name='detail')
]
