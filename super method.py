class car:
    def __init__(self,type):
        self.type =type

    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class toyotacar(car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
        super().stop()
        super().start()

car1 = toyotacar("prius", "electric") 
print(car1.type) 
