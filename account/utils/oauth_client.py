import requests
from urllib.parse import urlencode

from account.utils.constants import ShopifyOauth
from account.utils.helpers import get_host_url, response_to_dictionary


class ShopifyOauthClient:

    def __init__(self, shop_name: str, access_token: str = ""):
        self.shop_name = shop_name
        self.access_token = access_token

    def get_access_token(self, **data):
        res = requests.post(
            f"https://{self.shop_name}{ShopifyOauth.ACCESS_TOKEN_ENDPOINT}",
            data,
            timeout=60,
            verify=False
        )
        self.access_token = response_to_dictionary(res.text)['access_token']
        return self.access_token

    def get_shop_details(self):
        res = requests.get(
            f"https://{self.shop_name}{ShopifyOauth.SHOP_DETAILS_ENDPOINT}",
            headers={ShopifyOauth.ACCESS_TOKEN_HEADER: self.access_token}
        )
        shop_data = response_to_dictionary(res.text)['shop']

        return shop_data['email'], shop_data['shop_owner']

    def build_oauth_redirect_url(self, absolute_url):
        host = get_host_url(absolute_url)
        redirect_url = (
            f"https://{self.shop_name}{ShopifyOauth.AUTHORIZE_ENDPOINT}?"
            f"client_id={ShopifyOauth.API_KEY}&scope={ShopifyOauth.SCOPES}"
            f"&redirect_uri={host}{ShopifyOauth.REDIRECT_ENDPOINT}"
            f"&grant_options[]={ShopifyOauth.ACCESS_MODE}"
        )
        return redirect_url
