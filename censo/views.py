"""from django.shortcuts import render, get_object_or_404
from .models import Domicilio, Pessoa

def lista_domicilios(request):
    bairro = request.GET.get('bairro')
    cidade = request.GET.get('cidade')

    queryset = Domicilio.objects.all()

    if bairro:
        queryset = queryset.filter(bairro__icontains=bairro)

    if cidade:
        queryset = queryset.filter(cidade__icontains=cidade)

    context = {
        'domicilios': queryset,
        'bairro': bairro or '',
        'cidade': cidade or '',
        'total_domicilios': queryset.count(),
        'total_pessoas': Pessoa.objects.filter(domicilio__in=queryset).count()
    }

    return render(request, 'censo/lista_domicilios.html', context)


def pessoas_domicilio(request, domicilio_id):
    domicilio = get_object_or_404(Domicilio, id=domicilio_id)
    pessoas = domicilio.pessoas.all()

    return render(request, 'censo/pessoas_domicilio.html', {
        'domicilio': domicilio,
        'pessoas': pessoas
    })
"""