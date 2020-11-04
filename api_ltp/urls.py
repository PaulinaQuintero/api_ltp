
from linktopay.views import LinkToPayView
from django.urls import path


app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('ordertopay/', LinkToPayView.as_view()),
]
