def total_cost(request):
    total=0
    
    if request.user.is_authenticated:
        for key, value in request.session["car"].items():
            total=total+(float((value["quantity"]))*(value["price"]))
    
    return {"total_cost":total}