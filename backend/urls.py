from django.urls import path
from backend import views


urlpatterns = [
    path('loan/income/<int:income>/', views.HouseLoanAPIView.as_view(), name="loan-amount"),
]
