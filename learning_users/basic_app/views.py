from django.shortcuts import render
from .forms import UserForm, UserProfileForm

# Create your views here.


def user_profile(request):
    return render(request, 'basic_app/login.html')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pics' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        registered = False

    context = {'registration_form': user_form, 'userprofile_form': profile_form, 'registered': registered}
    return render(request, 'basic_app/registration.html', context=context)

