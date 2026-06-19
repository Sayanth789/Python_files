from diamond import A 

class U:
    def ping(self):
        print(f"{self}.ping() in U")
        super().ping() 

class LeafUA(U, A):
    def ping(self):
        print(f"{self}.ping() in LeafUA")
        super().ping()

class LeafAU(A, U):
    def ping(self):
        print(f'{self}.ping() in LeafAU')
        super().ping()

u = U
# print(u.ping())

leaf2 = LeafUA()
leaf2.ping()


o6 =  LeafAU()
print(o6.ping())

print(LeafAU.__mro__)

