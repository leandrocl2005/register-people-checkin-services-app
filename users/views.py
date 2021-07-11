from django.shortcuts import render


def user_profile_detail(request):
    return render(request, 'user_profile.html')
