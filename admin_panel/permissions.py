from django.shortcuts import redirect
from django.contrib.auth.models import AnonymousUser
from users.models import User # Auth User

class AdminLoginRequiredMixin:

    def dispatch(self, request, *args, **kwargs):
        rev_name = "home-page"
        no_auth = True
        if request.user.is_authenticated :
            if request.user.role == "admin":
                no_auth = False
        else:
            rev_name = "admin-login-page"

        if no_auth:
            return redirect(rev_name)
    
        return super().dispatch(request, *args, **kwargs)