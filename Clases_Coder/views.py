from django.http import HttpResponse

from django.template import Template, Context, loader


def saludo(request):
    return HttpResponse("Hola mundo!, hola Coder<br>Hola alumnos")

def muestra_nombre(request, nombre):
    return HttpResponse(f"Buenos dias {nombre}, bienvenido coder")

def probando_template(request):
    
    diccionario = {
        "first_name": "Diego",
        "last_name": "Segarra",
        "notas": [4,5,7,8,9,10]
    }
    # Abrimos el archivo html
    mi_html = open('./Clases_coder/plantillas/index.html')

    # Creamos el template haciendo uso de la clase Template
    plantilla = Template(mi_html.read())

    # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    mi_html.close()

    # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacío para que funcione
    mi_contexto = Context(diccionario)

    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)

def probando_template2(request):
    
    diccionario = {
        "first_name": "Diego",
        "last_name": "Segarra",
        "notas": [4,5,7,8,9,10]
    }
    
    plantilla = loader.get_template("index.html")
    
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)