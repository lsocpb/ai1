import random
import numpy

class Dres:
    def __init__(self, price, style, quality, marka):
        self.price = price
        self.style = style
        self.quality = quality
        self.marka = marka  # 0 - Nike, 1 - Adidas

    @staticmethod
    def generate_dres():
        price = random.randint(99, 499)
        style = random.random()
        quality = random.random()
        marka = random.randint(0, 1)
        return Dres(price, style, quality, marka)

    @staticmethod
    def generate_list(number):
        attributes = numpy.zeros((number, 3))
        labels = numpy.zeros((number, 1))
        for i in range(0, number):
            dres = Dres.generate_dres()
            attributes[i, 0] = dres.price
            attributes[i, 1] = dres.style
            attributes[i, 2] = dres.quality
            labels[i, 0] = dres.marka
        return attributes, labels
