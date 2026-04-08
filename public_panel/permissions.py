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


from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME


def user_login_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None
):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.role == "user",
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
