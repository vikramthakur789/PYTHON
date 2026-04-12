class person:
    name = 'vikram'
    # def changename(self,name):
    #     self.__class__.name = "goolu babu"

    @classmethod
    def changename(cls,name):
        cls.name = name

p1 = person()
p1.changename("golu babu")
print(p1.name)
print(person.name)        
