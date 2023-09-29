class Car:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        #Esto se hace para comparar en caso de que l usuario deja la pagina
        #y luego entra nuevamente a la pagina, se carga lo qe tenia
        car=self.session.get("car")

        #el diccionario es de la forma {id_producto1:{name,price,etc..},id_producto2:{name,price.etc..}}
        if not car:
            car=self.session["car"]={}
        
        #else:
        self.car=car
    
    def agregate(self, product):
        #Se evalua si el producto esta en el carro de comprar, si no esta se agrega
        if not str(product.id) in self.car.keys():
            self.car[product.id]={
                "product_id":product.id,
                "name":product.name,
                "price":str(product.price),
                "quantity":1,
                "image":product.image.url
            }
        else:
            quantity=self.car[product.id]["quantity"]
            self.car[product.id]["quantity"]=quantity+1
            """
            for key, value in self.car.items():
                if key==str(product.id):
                    value["quantity"]=value["quantity"]+1
                
            """
        #Esto va a actualizar la sesion cada vez que se haga una operacion en el carro
        self.save_car()
    
    def save_car(self):
        self.session["car"]=self.car
        self.session.modified=True
    
    def eliminate(self, product):
        product_id=str(product.id)
        if product_id in self.car:
            del self.car[product_id]
        self.save_car()
    
    def substract_product(self,product):
        for key, value in self.car.items():
            if key==str(product.id):
                value["quantity"]=value["quantity"]-1
                if value["quantity"]<=0:
                    self.eliminate(product)
            break
        #Esto va a actualizar la sesion cada vez que se haga una operacion en el carro
        self.save_car()

    def clean_car(self):
        self.session["car"]={}
        self.session.modified=True