# # i create this file for authenticate the user for the login
# from django.contrib.auth.backends import ModelBackend
# from .models import Users

# class UsersAuthenticationBackend(ModelBackend):
#     def authenticate(self, request, email=None, password=None, **kwargs):
#         try:
#             user = Users.objects.get(email=email)
#             if user.check_password(password):
#                 return user
#         except Users.DoesNotExist:
#             return None