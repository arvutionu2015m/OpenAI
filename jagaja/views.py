from django.shortcuts import render, redirect, get_object_or_404
from .forms import ÜlesanneVorm
from .models import Ülesanne, AlamÜlesanne
from .utils import jagatud_ülesanded
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.decorators.http import require_POST
from .utils import soovita_olulised_ülesanded

@login_required
def ai_soovitused(request):
    ülesanded = Ülesanne.objects.filter(kasutaja=request.user, tähtaeg__isnull=False, alamülesanded__tehtud=False).distinct()
    soovitus = soovita_olulised_ülesanded(ülesanded) if ülesanded.exists() else "Sul pole hetkel aktiivseid tähtajalisi ülesandeid."
    return render(request, 'ai_soovitused.html', {'soovitus': soovitus})



@require_POST
@login_required
def muuda_alamülesanne(request):
    alam_id = request.POST.get("alam_id")
    alam = get_object_or_404(AlamÜlesanne, id=alam_id, ülesanne__kasutaja=request.user)
    alam.tehtud = not alam.tehtud
    alam.save()
    return redirect('home')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def home(request):
    ülesanded = Ülesanne.objects.filter(kasutaja=request.user).prefetch_related('alamülesanded')

    tehtud_kokku = 0
    tegemata_kokku = 0

    for ülesanne in ülesanded:
        kokku = ülesanne.alamülesanded.count()
        tehtud = ülesanne.alamülesanded.filter(tehtud=True).count()
        ülesanne.progress_percent = int((tehtud / kokku) * 100) if kokku > 0 else 0

        tehtud_kokku += tehtud
        tegemata_kokku += (kokku - tehtud)

    return render(request, 'home.html', {
        'ülesanded': ülesanded,
        'tehtud_kokku': tehtud_kokku,
        'tegemata_kokku': tegemata_kokku,
    })

@login_required
def lisa_ülesanne(request):
    if request.method == 'POST':
        form = ÜlesanneVorm(request.POST, request.FILES)
        if form.is_valid():
            ülesanne = form.save(commit=False)
            ülesanne.kasutaja = request.user
            ülesanne.save()
            vastus = jagatud_ülesanded(ülesanne.kirjeldus)
            for rida in vastus.split('\n'):
                if rida.strip():
                    AlamÜlesanne.objects.create(ülesanne=ülesanne, sisu=rida.strip())
            return redirect('home')
    else:
        form = ÜlesanneVorm()
    return render(request, 'lisa_ülesanne.html', {'form': form})
