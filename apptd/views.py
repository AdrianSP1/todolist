from django.shortcuts import redirect,redirect, render
from .models import Tarea
from .forms import TareaForm


def home(request):
    tareas=Tarea.objects.all()
    context={'tareas':tareas}
    return render(request, 'apptd/home.html', context)

def agregar(request):
    if request.method =="POST":
        form=TareaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    else:
        form = TareaForm()
        context={}
        return render(request,'apptd/agregar.html',context)