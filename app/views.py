from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q

from app.models import Category, Review, Critic, Score
from app.forms import UserForm, CriticForm, ReviewForm

from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


# Pagina de inicio
# Vista principal

def main(request):
    user_form = UserForm(data=request.POST)
    critic_form = CriticForm(data=request.POST)
    if request.user.is_active:
        return HttpResponseRedirect('/feed')
    else:
        reviews = Review.objects.all().order_by('-pub_date')[:5]
        return render_to_response("index.html", {"reviews": reviews, "user_form":user_form, "critic_form":critic_form}, RequestContext(request)) 

@login_required(login_url='/login')	
def feed(request):
    context = RequestContext(request)
    categories = Category.objects.all()
    reviews = Review.objects.all().order_by('-pub_date')
    personal_reviews = Review.objects.all()
    if request.user.is_active:
        print request.user
    	critic = Critic.objects.get(user=request.user)
    	personal_reviews = Review.objects.all().order_by('-pub_date')
    return render_to_response("feed.html", {'categories': categories, 'reviews': reviews, 'user': request.user, 'personal_reviews': personal_reviews, 'critic': critic}, context)


def login(request):
    context = RequestContext(request)
    user = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/feed')
            else:
                pass
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return render_to_response("login_page.html", {"error": True, "username": username}, context)
    elif request.method == 'GET' and user is None: 
		return render_to_response("login_page.html", {"error": False}, context)
    else:
    	return render_to_response("login_page.html", {"error": True}, context)


def logout(request):
    context = RequestContext(request)
    auth_logout(request)
    return HttpResponseRedirect('/')

def register(request):
    context = RequestContext(request)
    username = request.POST['username']
    password = request.POST['password1']
    if request.method == 'POST':
    	form = UserForm(data=request.POST)
        critic_form = CriticForm()
        if form.is_valid():
            user = form.save()
            #user.set_password(user.password)
            user.save()

            critic = critic_form.save(commit=False)

            critic.user = user
            critic.image = 'http://tlprojects.com/ajax_local/pics/1.jpg'
            critic.save()
            user2 = authenticate(username=username, password=password)        
            if user2 is not None:
                if user.is_active:
                    auth_login(request, user2)
                    return HttpResponseRedirect('/feed')
                else:
                    pass
            else:
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:
        form = UserForm()
        return HttpResponseRedirect('/')

def profile(request, username):
    context = RequestContext(request)
    exists = False
    user = None
    critic = None
    try:
        user = User.objects.get(username=username)
        
    except:
        pass
    if request.user.is_active:
        critic = Critic.objects.get(user=request.user)
    if user is not None:
        exists = True
        f_critic = Critic.objects.get(user=user)
        reviews = Review.objects.filter(critic=f_critic).order_by('-pub_date')


    return render_to_response("profile.html", {"critic":critic, "f_critic": f_critic, "exists": exists, "reviews": reviews}, context)

@login_required(login_url='/login')
def user_profile(request):
    context = RequestContext(request)
    critic = Critic.objects.get(user=request.user)
    return render_to_response("user_profile.html", {"critic": critic}, context)

@login_required(login_url='/login')
def user_profile_configuration(request):
    context = RequestContext(request)
    critic = Critic.objects.get(user=request.user)
    return render_to_response("user_profile_configuration.html", {"critic": critic}, context)


def search(request):
    context = RequestContext(request)
    text = ""
    reviews = None
    critics = []
    critic = None

    if request.user.is_active:
        critic = Critic.objects.get(user=request.user)
    try:
        text = request.GET['text']
        reviews = Review.objects.filter(Q(title__icontains=text) | Q(content__icontains=text)).order_by('-pub_date')
        users = User.objects.filter(Q(username__icontains=text))

        for u in users:
            critics.append(Critic.objects.get(user=u))

        
    except:
        pass
    
    
    return render_to_response("search.html", {"critic": critic, "reviews": reviews, "critics": critics}, context)

def review(request, number):
    context = RequestContext(request)
    critic = None
    review = None
    isLiked = False
    u_score = 0
    try:
        review = Review.objects.get(id=number)
        review.readings = review.readings + 1;
        review.save()
        
            
        critic = Critic.objects.get(user=request.user)

        for score in review.scores.all():
            if score.critic == critic:
                isLiked = True
                u_score = score
    except Exception, e:
        pass
    
    return render_to_response("review.html", {'review':review, 'critic':critic, 'isLiked': isLiked, 'score':u_score}, context)

@login_required(login_url='/login')
def review_upload(request):
    context = RequestContext(request)
    critic = Critic.objects.get(user=request.user)
    categories = Category.objects.all()
    return render_to_response("review_upload.html", {"critic": critic, "categories":categories}, context)

@login_required(login_url='/login')
def ur(request):
    context = RequestContext(request)
    review = Review()
    review.content = request.POST['content']
    review.title = request.POST['title']
    review.category = Category.objects.get(id=request.POST['category'])
    review.readings = 0
    review.critic = Critic.objects.get(user=request.user)
    review.save()

    return HttpResponse(review.id)

@login_required(login_url='/login')  
def review_heart(request):
    score = Score()
    review = Review.objects.get(id=request.POST['review'])
    score.critic = Critic.objects.get(user=request.user)
    score.avg = 1
    score.save()

    review.scores.add(score)

    review.save()

    return HttpResponse(score.id)

@login_required(login_url='/login')  
def review_heart_delete(request):
    score = Score.objects.get(id=request.POST['score'])
    score.delete()

    return HttpResponse('OK')

def categories(request):

    return render_to_response("categories.html")

