from django.core import serializers
from django.shortcuts import render, get_list_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django_render_partial import templatetags
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from .models import Autos, Marcas, Modelos, Colores
from .forms import AutosForm


def index(request):
    return render(request, 'crud/index.html')


def get_autos(request):
    autos = Autos.objects.all()
    result = []
    for auto in autos:
        colores = []
        for color in auto.colores.all():
            colores.append(color.nombre)

        result.append(
            {
                "id": auto.id,
                "marca": auto.modelo_id.marcas_id.marca,
                "modelo": auto.modelo_id.modelo,
                "precio": auto.precio,
                "colores": ", ".join(colores),
                "descripcion": auto.descripcion
            }
        )
    return JsonResponse(result, safe=False)


def ins_auto(request):
    if request.method == 'POST':
        form = AutosForm(request.POST)
        if form.is_valid():
            precio = form.cleaned_data['precio']
            descripcion = form.cleaned_data['descripcion']
            modelo_id = form.cleaned_data['modelo_id']
            colores = form.cleaned_data['colores']

            auto = Autos.objects.create(
                precio=precio,
                descripcion=descripcion,
                modelo_id=modelo_id
            )

            for color in colores:
                auto.colores.add(Colores.objects.get(id=color.id))

            return JsonResponse({})

    else:
        form = AutosForm()

    return render(request, 'crud/ins_auto.html', {'form': form})


def get_marcas(request):
    if request.GET.get('search'):
        search = request.GET['search']
        marcas = Marcas.objects.filter(marca__contains=search)
    else:
        marcas = Marcas.objects.all()

    result = []
    for marca in marcas:
        result.append({
            "id": marca.id,
            "text": marca.marca
        })
    return JsonResponse(result, safe=False)


def get_modelos(request):
    marca = request.GET['marca']

    if request.GET.get('search'):
        search = request.GET['search']
        modelos = Modelos.objects.filter(modelo__contains=search)
    else:
        modelos = Modelos.objects.filter(marcas_id=marca)

    result = []
    for modelo in modelos:
        result.append({
            "id": modelo.id,
            "text": modelo.modelo
        })
    return JsonResponse(result, safe=False)


def get_colores(request):
    if request.GET.get('search'):
        search = request.GET['search']
        colores = Colores.objects.filter(nombre__contains=search)
    else:
        colores = Colores.objects.all()

    result = []
    for color in colores:
        result.append({
            "id": color.id,
            "text": color.nombre
        })
    return JsonResponse(result, safe=False)


def upd_auto(request, auto_id):
    if request.method == 'POST':
        form = AutosForm(request.POST)
        if form.is_valid():
            precio = form.cleaned_data['precio']
            descripcion = form.cleaned_data['descripcion']
            modelo_id = form.cleaned_data['modelo_id']
            colores = form.cleaned_data['colores']

            auto = Autos.objects.create(
                precio=precio,
                descripcion=descripcion,
                modelo_id=modelo_id
            )

            for color in colores:
                auto.colores.add(Colores.objects.get(id=color.id))

            return JsonResponse({})

    else:
        auto = Autos.objects.select_related(
            'modelo_id', 'modelo_id__marcas_id').get(id=auto_id)

        colores = Colores.objects.raw(
            'SELECT * FROM crud_autos a inner join crud_autos_colores ac on a.id = ac.autos_id where a.id = %s', [auto_id])

        colores_selected = []
        for color in colores:
            colores_selected.append(color.colores_id)

        form = AutosForm({
            'marcas_id': auto.modelo_id.marcas_id,
            'modelo_id': auto.modelo_id,
            'precio': auto.precio,
            'colores': colores_selected,
            'descripcion': auto.descripcion
        })

    return render(request, 'crud/upd_auto.html', {'form': form})
