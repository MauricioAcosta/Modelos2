#!/usr/bin/python3
from n_ario_predictor import Predictor
predictor = Predictor()
while True:
    entrada = input("Ingrese una palabra: ")
    if len(entrada)>0:
        print("Tal vez quiso decir: " + predictor.buscarPorPalabra(entrada))
