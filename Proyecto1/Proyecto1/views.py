from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

# crear primera vista
# cada funcion es una vista, donde se devuelve el texto
def saludo(request):
    path="./Proyecto1/templates/first_template.html"
    doc=open(path)
    plt=Template(doc.read())
    doc.close()
    ctx=Context()
    response=plt.render(ctx)

    return HttpResponse(response)

# segundavista
# en este codigo se puede ver como no se utiliza templates, no se debe hacer
'''
def get_time(request):
    time=str(datetime.datetime.now())
    response="""<html>
                <head>
                <style>
                    h1 {
                    color: blue;
                    font-family: Arial;
                    text-align: center;
                    }
                </style>
                </head>
                <body>
                    <h1>"""+time+"""</h1>
                </body>
                </html>
                """
    return HttpResponse(response)
'''
# segunda vista con templates, se enseña a como usar variables dentro de los 
# templates, la manera correcta es creando un diccionario en view de clave: valor
# y en el template se hace referencia a la variable con dos corchetes {{variable}}
# el nombre de la variable es la key
def get_time(request):
    time=datetime.datetime.now()

    # 2. metodo usado sin usar el loader 
    '''
    Este forma de cargar el template no se suele usar por el consumo de recursos,
    en este caso este el codigo:
    1. Abre un documento, almacena el contenido en doc, usando Template
    2. Se determina el conjunto de variables a usar en el contexto.
    3. Se renderiza el contexto.

    en lugar de ellos se usa LOADER el cual se debe importar
    path="./Proyecto1/templates/first_template.html"
    doc=open(path)
    plt=Template(doc.read())
    doc.close()
    ctx=Context({"actual_time":time})
    response=plt.render(ctx)
    '''

    # 3.Usando el metodo LOADER
    '''
    1. importar loader
    2. en el script settings.py en "DIRS":configurar el path donde se encuentran los 
        templates.
    3. obtener el documento usando get_template()
    4. el contexto sera un diccionario simple, ya no se instacia Context esto para
        que no ocurran problemas cuando se renderice.
    
    doc=loader.get_template("first_template.html")
    ctx={"actual_time":time}
    response=doc.render(ctx)
    '''

    # 4. usando Django.shortscuts
    '''
    Se cuenta con una opcion mas facil de render, con django.shorcuts donde solo
    se necesita una sola linea, creando una instancia de render ya se ejecuta
    un http response, los argumentos van en la llamada al metodo: 
    '''
    ctx={"actual_time":time}
    return render(request,"template.html",ctx)

    # usarser con el metodo 2 y 3
    #return HttpResponse(response)
'''
def bar_nav(request):
    return render(request,"template_2.html")
'''

def images(request):
    return render(request, "secctions/images.html")


# tercera vista operaciones con variables enviados en el path
def age_estimate(request, year_future, year_actual):
    age=(year_future - year_actual)
    return HttpResponse(
        "<html><body><h2>En el "+str(year_future)+" tendras: "+str(age)+" años<h2><body><body>")
