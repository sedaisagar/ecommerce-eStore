from django.shortcuts import redirect
from django.contrib.auth.models import AnonymousUser
from users.models import User # Auth User

class UserLoginRequiredMixin:

    def dispatch(self, request, *args, **kwargs):
        rev_name = "login-page"

        no_auth = True
        if request.user.is_authenticated :
            if request.user.role == "user":
                no_auth = False
            else:
                no_auth = True
                rev_name = "admin-home-page"
       
        if no_auth:
            return redirect(rev_name)
        return super().dispatch(request, *args, **kwargs)
    
class UserLoginCheckRequiredMixin:

    def dispatch(self, request, *args, **kwargs):
        rev_name = "home-page"

        no_auth = False
        if request.user.is_authenticated :
            if request.user.role == "user":
                no_auth = True
     
        if no_auth:
            return redirect(rev_name)
    
        return super().dispatch(request, *args, **kwargs)