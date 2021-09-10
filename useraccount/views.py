from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from .token import account_activation_token
from django.http import HttpResponse
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from useraccount.models import UserBase

# Create your views here.


def account_register(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save()
            user.email = registerForm.save(commit=False)
            user.set_email(registerForm.cleaned_data['email'])
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('useraccount/registration/accountactivation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)
            return HttpResponse('registered succesfully and activation sent')
    else:
        registerForm = RegistrationForm()
    return render(request, 'registration/signup.html', {'form': registerForm})


@login_required
def dashboard(request):
    orders = user_orders(request)
    return render(request,
                  'user/dashboard.html',
                  {'section': 'profile', 'orders': orders})

def activation(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('account:dashboard')
    else:
        return render(request, 'registration/activation_invalid.html')





