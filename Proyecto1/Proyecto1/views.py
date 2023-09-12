from django.http import HttpResponse
import datetime
from django.template import Template, Context

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
    path="./Proyecto1/templates/first_template.html"
    doc=open(path)
    plt=Template(doc.read())
    doc.close()
    time=datetime.datetime.now()
    ctx=Context({"actual_time":32})

    response=plt.render(ctx)

    return HttpResponse(response)


# tercera vista operaciones con variables enviados en el path
def age_estimate(request, year_future, year_actual):
    age=(year_future - year_actual)
    return HttpResponse(
        "<html><body><h2>En el "+str(year_future)+" tendras: "+str(age)+" años<h2><body><body>")
