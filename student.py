

class Student:


    """Student classi"""


    def __init__(self,full_name,univer,gpa,kursi):
        self._full_name = full_name
        self._univer = univer
        self._gpa  = gpa
        self._kursi = kursi

    def get_full_name(self):
        return  f"F.I.SH: {self._full_name}"

    def get_univer(self):
        return  self._univer.get_name()
    def get_gpa(self):
        return  self._gpa
    def get_kurs(self):
        return  self._kursi

    def set_kurs(self):
        if self._kursi<4:

            self._kursi+=1
    def tanishtir(self):
        print(f"Mening ishmim : {self._full_name}"
              f"Mening universitetim: {self._univer.get_name()}"
              f"Mening gpa: {self._gpa}"
              f"Men {self._kursi} da oqiyman")

