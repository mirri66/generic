from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Question, User
from .forms import UserForm, UserProfileForm


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    user = request.user
    context = {'latest_question_list': latest_question_list, 'user':user}
    return render(request, 'puzzles/index.html', context)

#### question detail ####
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'puzzles/detail.html', {'question': question})

#### users profile####
def profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    userprofile = get_object_or_404(User, pk=user_id)
    team_members = [{'name':'Siti Mariam','id':0, 'remaining':45,'total':400}, {'name':'Kasturi Raju','id':1, 'remaining': 15,'total':350}, {'name':'Jessica Rajaratnam', 'id':2, 'remaining': 85,'total':300}, {'name':'Angel Widjojo', 'id':3, 'remaining':100,'total':250}, {'name':'Shana Salim', 'id':4, 'remaining':80,'total':530}]

    return render(request, 'puzzles/profile.html', {'user': user, 'userprofile':userprofile, 'team_members':team_members})


#### login / signup ####
def login_view(request):
    return render(request, 'puzzles/login.html')

def logout(request):
    logout(request)
    return redirect('index')

def postlogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    return render(request, 'puzzles/index.html')

#### payment ####
def pay_view(request):
    return render(request, 'puzzles/pay.html')

def postpay(request):
    amount = request.POST['amount']
    return render(request, 'puzzles/thankyou.html')

def signup(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            profile = profile_form.save(commit=False)
            profile.user = user

            ## Did the user provide a profile picture?
            ## If so, we need to get it from the input form and put it in the UserProfile model.
            #if 'picture' in request.FILES:
            #    profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True
            return redirect('index') 

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'puzzles/signup.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

