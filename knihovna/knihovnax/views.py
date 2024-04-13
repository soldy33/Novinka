from django.shortcuts import render, reverse, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Knihovna
from .serializers import KnihovnaSerializer
from django.http import HttpResponseRedirect

class KnihovnaViewSet(viewsets.ModelViewSet):
    queryset = Knihovna.objects.all()
    serializer_class = KnihovnaSerializer


from django.shortcuts import render, redirect, get_object_or_404
from .models import Knihovna

def zobrazit_tabulku_a_smazat_knihu(request):
    knihovna_list = Knihovna.objects.all()
    if request.method == 'POST':
        selected_knihovna_ids = request.POST.getlist('selected_knihovna_ids')
        Knihovna.objects.filter(id__in=selected_knihovna_ids).delete()
        return redirect('smazat_knihu_tabulka')
    return render(request, 'tabulka_a_smazat_knihu.html', {'knihovna_list': knihovna_list})

def knihovna_tabulka(request):
    knihovna_list = Knihovna.objects.all()
    Knihovna.vraceni_knihy()
    return render(request, 'knihovna_tabulka.html', {'knihovna_list': knihovna_list})

def prodlouzit_vypujcku(request, knihovna_id):
    kniha = Knihovna.objects.get(pk=knihovna_id)
    kniha.prodlouzit_vypujcku()
    return HttpResponseRedirect(reverse('knihovna_tabulka'))

