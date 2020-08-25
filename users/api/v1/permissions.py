# class ShopifyCustomerPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if type(request.data) is not dict:
#             request.data._mutable = True
#
#         if 'STOREFRONT-CUSTOMER-ACCESS-TOKEN' in request.headers:
#             customer_access_token = request.headers['STOREFRONT-CUSTOMER-ACCESS-TOKEN']
#             # print(customer_access_token)
#             access_token = storefront_customer_data(customer_access_token)
#             if access_token:
#                 request.data['graphql_customer_id'] = access_token['id']
#                 customer_id = graphql_id_to_integer(access_token['id'])
#                 request.data['customer_id'] = customer_id
#                 # print(access_token['id'])
#                 return True
#             else:
#                 return False
#         else:
#             return False
