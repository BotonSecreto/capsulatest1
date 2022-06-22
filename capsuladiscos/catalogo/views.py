from django.shortcuts import render, get_object_or_404
from .models import Disco, Banda, IntegranteBanda, Musico, ProduccionDisco #importar el modelo
# Create your views here.
def catalogo(request):
    #recupera todos los objetos de las clases
    discos = Disco.objects.all() 
    #bandas = Banda.objects.all()
    #musicos = Musico.objects.all()
    #produccionDisco = ProduccionDisco.objects.all()
    #integranteBanda = IntegranteBanda.objects.all()
    #*****ruta actualizada al MVT que
    return render(request, "catalogo/catalogo.html",{'discos':discos}) #Inyecta datos en página html
    #return render(request, "catalogo/catalogo.html",{'discos':discos},{'bandas':bandas}) #Inyecta datos en página html
    #return render(request, "catalogo/catalogo.html",{'discos':discos},{'bandas':bandas},{'musicos':musicos}) #Inyecta datos en página html

    #**************
def disco(request, disco_id):
    disco = get_object_or_404(Disco, id=disco_id) #evitar el error 404 por pág desconocida con "get"
    #banda = Banda.objects.all()
    #musico = Musico.objects.all()
    produccionDisco = ProduccionDisco.objects.all()
    #integranteBanda = IntegranteBanda.objects.all()
    return render(request, "catalogo/disco.html", {'disco':disco,'produccionDisco':produccionDisco}) #Inyecta datos en página html
    #return render(request, "catalogo/disco.html", {'disco':disco}, {'banda':banda}) #Inyecta datos en página html

    #**************************
def banda(request, banda_id):
    banda = get_object_or_404(Banda, id=banda_id) #evitar el error 404 por pág desconocida con "get"
    musico = Musico.objects.all()
    integranteBanda = IntegranteBanda.objects.all()
    discos = Disco.objects.all() 
    return render(request, "catalogo/banda.html", {'banda':banda,'musico':musico,'integranteBanda':integranteBanda,'discos':discos}) #Inyecta datos en página html

    #**************************
def musico(request, musico_id):
    musico = get_object_or_404(Musico, id=musico_id) #evitar el error 404 por pág desconocida con "get"
    produccionDisco = ProduccionDisco.objects.all()
    integranteBanda = IntegranteBanda.objects.all()
    return render(request, "catalogo/musico.html", {'musico':musico, 'produccionDisco':produccionDisco, 'integranteBanda':integranteBanda}) #Inyecta datos en página html