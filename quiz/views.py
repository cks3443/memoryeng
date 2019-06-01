from django.shortcuts import render, HttpResponseRedirect, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from random import randrange, random, choice
from .models import Sentence, History

from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .customsignform import UserCreateForm

# from .forms import UserForm, LoginForm, User
# Create your views here.


def index(request):
    global t, ee
    # print('============= {} =============='.format(request.user))
    while True:
        rn = random()
        if not request.user.is_authenticated:
            rn = 0.4
        try:

            if rn < 0.5:
                # print('not login , {}'.format(rn))
                cc = Sentence.objects.count()
                t = randrange(0, cc)
                ee = Sentence.objects.all()[t]
            else:
                # print('login , {}'.format(rn))
                hpk = History.objects.filter(user=request.user).filter(Q(level='MI') | Q(level='HI'))
                if len(hpk) is 0:
                    continue
                ee = choice(hpk).quiz

            break
        except ObjectDoesNotExist:
            continue

    return render(request, 'quiz/home.html', {'ko': ee.kosub, 'en': ee.ensub, 'pk': ee.pk, 'action': '/recording'})


def recording(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')

    data = request.GET.copy()
    old_pk = data['old_pk']
    level = data['level']
    _in = data['in']

    global quiz

    # print("old_pk: {}, level: {}, in: {}".format(old_pk, level, _in))

    if _in.strip() is not '':
        user = request.user
        try:
            quiz = Sentence.objects.get(pk=old_pk)
            archive = History.objects.get(Q(user=user) & Q(quiz=quiz))
            archive.level = level
            archive.save()
        except ObjectDoesNotExist:
            h = History(user=user, quiz=quiz, level=level)
            h.save()

    return HttpResponseRedirect('/')


def sign(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(email=email, passwrod=raw_password)
            login(request, user)
            return redirect('/')

    else:
        form = UserCreateForm()
        return render(request, 'quiz/Sign.html', {'form': form})

    return redirect('/')
