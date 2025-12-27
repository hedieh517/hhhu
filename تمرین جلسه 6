#جلشه ششم کلاس والد و فرزند
class vehicle:
    def __init__(self , brand , year):
        
        self.brand = brand
        self.year = year
        
    def display_info(self):
        print(f"brand : {self.brand} , year : {self.year}")
        
class car(vehicle):
    def __init__(self , brand , year , num_doors):
        vehicle.__init__(self , brand , year)
        self.num_doors = num_doors
        
    def display_info(self):
        vehicle.display_info(self)
        print(f"extra number of doors: {self.num_doors}")
        
   
class motorcycle(vehicle):
    def __init__(self , brand , year , has_sidecar):
        vehicle.__init__(self , brand , year)
        
        self.has_sidecar = has_sidecar
        
    def display_info(self):
        vehicle.display_info(self)
        print(f"ezafe kardn has_sidecar: {self.has_sidecar}")
            
v = vehicle("mazda" , 2004)
v.display_info() 

c = car("benz" , 2010 , 4)
c.display_info() 

m = motorcycle("bmw" , 2025  ,True)
m.display_info()         
            
            
            
            
            
            
            
        
        
        
        
        
