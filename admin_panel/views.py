from django.views import generic
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

class AdminLoginView(generic.TemplateView):
    template_name = "admin-panel/auth-login-basic.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == "admin":
            return redirect("admin-home-page")
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")


        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("admin-home-page")
        else:
            context = self.get_context_data()
            context["error"] = "Invalid credentials."
            return self.render_to_response(context)

class AdminHomeView(generic.TemplateView):
    template_name = "admin-panel/index.html"


