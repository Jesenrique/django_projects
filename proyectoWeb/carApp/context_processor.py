def total_cost(request):

    total=0
    if request.user.is_authenticated:
       for key, value  in request.session["car"].items():
        total=total+float(value["price"])
    else:
       total="Inicia sesión para ver el total"
    return {"total_cost":total}