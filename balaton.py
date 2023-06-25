import unittest
class Teszt(unittest.TestCase):
    f = open("utca.txt", "r")
    adosavok_sor= f.readline()
    adosavok = {
        "A": int(adosavok_sor.split(' ')[0]),
        "B": int(adosavok_sor.split(' ')[1]),
        "C": int(adosavok_sor.split(' ')[2])
    }
    f.close()
    def test1(self):
        self.assertEqual(ado("C",180),18000)
        self.assertEqual(ado("B",56),33600)
        self.assertEqual(ado("A",120),96000)
        
    def test2(self):
        self.assertEqual(ado("C",164),0)

class Telek:
    def __init__(self, adoszam, utca, hazszam, adosav, alapterulet):
        self.adoszam = int(adoszam)
        self.utca = utca
        self.hazszam = hazszam
        self.adosav = adosav
        self.alapterulet = int(alapterulet)

        @property
        def adoszam(self):
            return self.adoszam
        
        @property
        def utca(self):
            return self.utca
        
        @property
        def hazszam(self):
            return self.hazszam
        
        @property
        def adosav(self):
            return self.adosav

        @property
        def alapterulet(self):
            return self.alapterulet

def ado(adosav, alapterulet):
    return adosavok[adosav] * alapterulet if adosavok[adosav] * alapterulet>10000 else 0

utca =list()

f = open("utca.txt", "r")
adosavok_sor= f.readline()
adosavok = {
    "A": int(adosavok_sor.split(' ')[0]),
    "B": int(adosavok_sor.split(' ')[1]),
    "C": int(adosavok_sor.split(' ')[2])
}
for x in f:
    line = x.split(' ')
    utca.append(Telek(line[0],line[1],line[2],line[3],line[4]))
f.close()

#2
print("2. feladat. A mintában", len(utca), "telek szerepel")

#3
egyadoszam = int(input("3. feladat. Egy tulajdonos adószáma: "))

talalat = False
A_db = 0
A_osszado = 0
B_db = 0
B_osszado = 0
C_db = 0
C_osszado = 0
for x in utca:
    if egyadoszam == x.adoszam:
        talalat = True
        print(x.utca, "utca", x.hazszam)

    telekado = ado(x.adosav, x.alapterulet)
    if x.adosav == "A":
        A_db += 1
        A_osszado += telekado
    elif x.adosav == "B":
        B_db += 1
        B_osszado += telekado 
    else:
        C_db += 1
        C_osszado += telekado 

if talalat == False:
    print("Nem szerepel az adatállományban.")
print("5. feladat\nA sávba", A_db, "telek esik, az adó", A_osszado, "Ft.\nB sávba", B_db, "telek esik, az adó", B_osszado, "Ft.\nC sávba", C_db, "telek esik, az adó", C_osszado, "Ft.")

teljes = open("teljes.txt", "w")
for x in utca:
    sor = f"{x.adoszam} {x.utca} {x.hazszam} {x.adosav} {x.alapterulet} {ado(x.adosav, x.alapterulet)}\n"
    teljes.write(sor)
teljes.close()
unittest.main()
