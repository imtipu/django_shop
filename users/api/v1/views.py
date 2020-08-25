import requests
from django.http import HttpResponse, Http404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.api.v1.serializers import *


def account_login(request):
    return HttpResponse(0)


class AuthenticatedUserProfile(RetrieveAPIView, UpdateAPIView):
    authentication_classes = [JWTAuthentication,
                              SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserLoggedSerializer

    def get_object(self):
        try:
            return User.objects.get(pk=self.request.user.id)
        except User.DoesNotExist:
            raise Http404


class CustomerLoginVerify(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    @staticmethod
    def get(request):
        access_token = request.headers['STOREFRONT-CUSTOMER-ACCESS-TOKEN']
        url = "https://boboandmusu.myshopify.com/api/2020-07/graphql.json"
        storefront_token = '5247469c1fe5ed4320548cf49eb01d66'
        query = '''
                query
                    {
                        customer(customerAccessToken: "%s") {
                            id
                            lastName
                            firstName
                            email
                        }
                    }
                ''' % access_token

        headers = {
            'X-Shopify-Storefront-Access-Token': storefront_token.encode('idna').decode('utf-8'),
            'Content-Type': 'application/json',
        }

        response = requests.request("POST", url, headers=headers, json={'query': query})
        # values = {'query': query}
        # data = json.dumps(values).encode('utf-8')
        # # response = urllib.request.Request(url, data, headers)
        # req = urllib.request.Request(url, data, headers)
        # with urllib.request.urlopen(req) as f:
        #     res = f.read()
        #
        # res_json = json.loads(res.decode())

        # print(res_json['data']['customer'])
        res_json = response.json()
        if res_json['data']['customer'] is not None:
            # print(res_json['data']['customer'])
            # return res_json['data']['customer']
            return Response(res_json['data']['customer'])
        else:
            return Response(res_json)
