from django.shortcuts import render, get_object_or_404
from .models import Usta, IshTuri


def splash(request):
    return render(request, "splash.html")
def base(request):
    return render(request, "base.html")


def navigation(request):
    return render(request, "navigation.html")


def footer(request):
    return render(request, "footer.html")
def home(request):
    
    ustalar = Usta.objects.all()
    ishlar = IshTuri.objects.all()

    selected_ish = request.GET.get('ish', '').strip()
    if selected_ish:
        ustalar = ustalar.filter(ishlar__id=selected_ish)

    selected_shahar = request.GET.get('shahar', '')
    if selected_shahar:
        ustalar = ustalar.filter(shahar=selected_shahar)

    context = {
        'ustalar': ustalar,
        'ishlar': ishlar,
        'selected_ish': selected_ish,
        'selected_shahar': selected_shahar,
    }
    return render(request, 'home.html', context)



def usta_filter(request):
    ustalar = Usta.objects.all()
    ish_id = request.GET.get('ish')
    shahar = request.GET.get('shahar')
    favqulodda = request.GET.get('favqulodda')

    # MANY-TO-MANY filter
    if ish_id:
        ustalar = ustalar.filter(ishlar__id=ish_id).distinct()

    if shahar:
        ustalar = ustalar.filter(shahar=shahar)

    if favqulodda == '1':
        ustalar = ustalar.filter(favqulodda=True)

    html = render_to_string('ustalar_list.html', {'ustalar': ustalar})
    return JsonResponse({'html': html})


def usta_profile(request, usta_id):
    usta = get_object_or_404(Usta, id=usta_id)
    return render(request, 'profile.html', {'usta': usta})


def seting(request):
    return render(request, 'seting.html')

def user_profile(request):
    return render(request, "user.html")


def all_masters(request):
    ustalar = Usta.objects.all()  
    return render(request, "all_masters.html", {
        'ustalar': ustalar
    })
    
def evukator(request):
    return render(request, "evakuator.html")


def my_avto(request):
    return render(request, "my_avto.html")