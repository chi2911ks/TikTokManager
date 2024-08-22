# -*- coding: utf-8 -*-

import random
from unidecode import unidecode


class GeneratorName:
    def __init__(self, fileName):
        with open(fileName, encoding="utf-8") as file:
            names = file.read().splitlines()
            self.name = random.choice(names)
    @property
    def fullname(self):
            return self.name
    @property
    def username(self):
        return unidecode(self.name.lower()).replace(" ", "")+str(random.randint(10, 99))
# if rd1.isChecked(): 
# elif rd2.isChecked():
# elif rd3.isChecked():
# elif rd4.isChecked():