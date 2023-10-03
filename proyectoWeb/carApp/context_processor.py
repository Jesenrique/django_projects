def total_cost(request):

    total=0
    for product in request.session["car"].values():
        total=product["subtotal"]+total
    
    return {"total_cost":total}