from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

from users.models import User

class LoginPageView(generic.TemplateView):
    template_name = "public-panel/login.html"
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None and user.role == "user":
            login(request, user)
            return redirect("admin-home-page")
        else:
            context = self.get_context_data()
            if user:
                context["error"] = "Invalid credentials, admin are not allowed here."
            else:
                context["error"] = "Invalid credentials"
            return self.render_to_response(context)

class RegisterPageView(generic.TemplateView):
    template_name = "public-panel/register.html"
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        if not all([username, password, email, first_name, last_name]):
            context = self.get_context_data()
            context["error"] = "All fields are required."
            return self.render_to_response(context)

        if User.objects.filter(username=username).exists():
            context = self.get_context_data()
            context["error"] = "Username already exists."
            return self.render_to_response(context)

        User.objects.create(
            username=username, 
            password=make_password(password), 
            email=email, 
            first_name=first_name, 
            last_name=last_name, 
        )
        return redirect("login-page")

class HomePageView(generic.TemplateView):
    template_name = "public-panel/index.html"

class AboutPageView(generic.TemplateView):
    template_name = "public-panel/about.html"