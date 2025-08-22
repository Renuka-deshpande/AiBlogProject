from django.shortcuts import render , redirect
from.models import CustomUser, Profile

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']

        user = CustomUser.objects.create(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save()

        Profile.objects.create(user=user)

        return redirect('login')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = CustomUser.objects.get(username=username)
            if user.check_password(password):
                request.session['user_id'] = user.id
                return redirect('dashboard')
            else:
                return render(request, 'login.html', {'error': 'Invalid password'})
        except CustomUser.DoesNotExist:
            return render(request, 'login.html', {'error': 'User does not exist'})
    return render(request, 'login.html')

def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return redirect('login')

def profile(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    user = CustomUser.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        profile.bio = request.POST['bio']
        profile.website = request.POST['website']
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']
        profile.save()
        return redirect('profile')

    return render(request, 'profile.html', {'user': user, 'profile': profile})

