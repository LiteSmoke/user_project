from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from .models import UserInfo
from .forms import UserInfoForm, UserProfileForm, UserForm
from django.core.exceptions import ValidationError
from django.conf import settings
import os

# Create your views here.

def index(request):

    return render(request, 'user_app/index.html', {})

def process_profile_icon(f):
    filename = os.path.join(settings.MEDIA_ROOT, f.name)
    # print(filename)
    with open(filename, 'wb+') as dest_file:
        for chunk in f.chunks():
            dest_file.write(chunk)

def register(request):

    user_form = UserForm(initial = {'username':'test1',
                                    'password':'pass12345',
                                    'email':'test@test.ru',
                                    'first_name':'First Name',
                                    'last_name':'Last name'})
    user_info_form = UserInfoForm(initial = {   'comment':'bla bla bla',
                                                })

    if request.method == 'POST':

        user_form = UserForm(request.POST)
        user_info_form = UserInfoForm(request.POST, request.FILES)
        # user_info_form = UserInfoForm(request.POST)

        if user_form.is_valid() and user_info_form.is_valid():

            user = user_form.save()
            user_info = user_info_form.save(commit=False)
            user_info.user = user
            user_info.save()

            # TODO save profile_icon

            # if 'profile_icon' in request.FILES:
            #
            #     profile_icon = request.FILES['profile_icon']
                # process_profile_icon(request.FILES['profile_icon'])

            return HttpResponseRedirect(reverse('index'))

        else:
            print("INVALID FORM INFORMATION!")

            print('user_form errors:', len(user_form.errors))
            print('user_info_form errors:', len(user_info_form.errors))

            for (field, errors) in user_form.errors.items():
                print(field, errors)

            for (field, errors) in user_info_form.errors.items():
                print(field, errors)

            # raise ValidationError("FORM VALIDATION ERROR")

    return render(request, 'user_app/register.html', {'user_form':user_form, 'user_info_form': user_info_form})

def user_login(request):

    dict = {'message':{
                'text':'',
                'type':''}}

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))

        else:
            # raise ValidationError("Wrong username or password")
            dict['message']['text'] = "Wrong username or password"
            dict['message']['type'] = 'error'
            # print("Wrong username or password")
            return render(request, 'user_app/login.html', context=dict)
    else:
        print("login page")

        return render(request, 'user_app/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def profile(request):

    # get current loginned user
    # user = User(current)

    user_form = UserForm(instance = user)
    user_info_form = UserInfoForm(instance = UserInfoForm.objects.get(user = user))

    # if Save button clicked
    if request.method == 'POST':

        # initiate just some fields, like username, password, email
        user_form = UserForm(request.POST, instance = request.user)

        user_info_form = UserInfoForm(request.POST, instance = UserInfoForm.objects.get(user = user))

        if user_form.is_valid() and user_info_form.is_valid():

            user_form.save()
            user_info_form.save()

            print("Profile information was updated successfully")

            # or just register
            return HttpResponseRedirect(reverse('user_app/register', kwargs={'result':'successful'}))

        else:
            raise ValidationError("FORM VALIDATION ERROR")
            # add form validation message
            print("FORM VALIDATION ERROR")

    return render(request, 'user_app/user_profile.html', {'result':'successful'})

@login_required
def download_user_file(request):
    pass
