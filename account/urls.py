from django.urls import path
from account import views

app_name = "account"

urlpatterns = [
    path('oauth/shopify/',
         views.ShopifyOauthRedirectAPIView.as_view(), name='oauth-redirect-shopify'),
    path('oauth/shopify/authorize/',
         views.ShopifyUserCreationAPIView.as_view(), name='oauth-authorize-shopify'),
]