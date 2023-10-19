from imaplib import _Authenticator
from trips.models import *
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from trips.forms import *

def home(request):
    trips = Trip.objects.all()
    return render(request, 'home.html', {'trips': trips})

def trip_detail(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    return render(request, 'trip_detail.html', {'trip': trip})

def register(request):
    if request.method == 'POST':
    # Get form values
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
    else:
        return render(request, 'register.html')

    # Check if passwords match
    if password == password2:
      # Check username
        if User.objects.filter(username=username).exists():
            messages.error(request, 'That username is taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
                messages.error(request, 'That email is being used')
                return redirect('register')
        else:
          # Looks good
          user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
          # Login after register
          # auth.login(request, user)
          # messages.success(request, 'You are now logged in')
          # return redirect('index')
          user.save()
          messages.success(request, 'You are now registered and can log in')
          return redirect('login')
    else:
      messages.error(request, 'Passwords do not match')
      return redirect('register')



"""    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #form.save()
            login(request, form.instance)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
"""
def user_login(request):
    user = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

    """if request.method == 'POST':
        # Handle login form submission
        username = request.POST['username']
        password = request.POST['password']
        #user = _Authenticator(username=username, password=password)
        from django.contrib.auth import authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            # Invalid login credentials
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')"""

def user_logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('login')

    """logout(request)
    return redirect('login')
"""

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'form': form})


def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'create_booking.html', {'form': form})

def booking_success(request):
    return render(request, 'booking_success.html')

def manage_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'manage_bookings.html', {'bookings': bookings})


def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('review_success')
    else:
        form = ReviewForm()
    return render(request, 'submit_review.html', {'form': form})

def review_success(request):
    return render(request, 'review_success.html')

def trip_reviews(request, trip_id):
    reviews = Review.objects.filter(trip_id=trip_id)
    return render(request, 'trip_reviews.html', {'reviews': reviews})

def calculate_average_rating(request, trip_id):
    reviews = Review.objects.filter(trip_id=trip_id)
    if reviews:
        total_ratings = sum(review.rating for review in reviews)
        average_rating = total_ratings / len(reviews)
        return average_rating
    else:
        return 0