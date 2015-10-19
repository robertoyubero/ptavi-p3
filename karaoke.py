#author>> Roberto Yubero
#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler
import sys
import urllib
import json

class KaraokeLocal():
    my_tags = []

    def __init__ (self, ficheroSmil):
        #parseo el fichero
        parser = make_parser()
        smilHandler = SmallSMILHandler()
        parser.setContentHandler(smilHandler)
        parser.parse(open(ficheroSmil, 'r'))
        #obtengo etiquetas
        self.my_tags = smilHandler.get_tags()
        #con el metodo init no puedo usar return >> uso my_tags como v.global

    def __str__(self):
        string_salida = ""
        #1-busco etiqueta
        for elemento in self.my_tags:
            etiqueta = elemento[0]
            diccionario = elemento[1]
            """2-compruebo que los atributos no esten vacios
                #2a-no esta vacia >> guardo etiqueta
                #2b-esta vacia >> paso a la  siguiente etiqueta
            """
            mis_atributos = ""
            for atributo in diccionario.keys():
                if diccionario[atributo] != "":
                    mis_atributos += "\t" + atributo + '="' + diccionario[atributo] + '"'
            string_salida += etiqueta + mis_atributos + "\n"

        return string_salida

    def do_local(self):
        #1-busco etiqueta
        """ 1)recorro la lista y voy extrayendo el diccionario de atributos de cada etiqueta
            2)con diccionario miro sus atributos y busco el atributo == src
            3)al atributo == src >> descargo su contenido
                                 >> cambio el valor de diccionario[atributo]
        """
        for i in range(0, len(self.my_tags)):
            dicc = self.my_tags[i][1]
            for atributo in dicc.keys():
                if atributo == "src":
                    dicc[atributo] = self.get_multimedia(dicc[atributo])

    def get_multimedia(self, valor_entrada):
        #si tiene url la descargo y cambio nombre e imprimo
        if valor_entrada[:7] == "http://":
            #recorto el nombre del archivo a descargar
            name_archivo = valor_entrada.rsplit('/')[-1]
            #descargo la url
            urllib.urlretrieve(valor_entrada, name_archivo)
        else:
            name_archivo = valor_entrada
        return name_archivo

    def to_json(self, fichero_smil):
        json.dump(fichero_smil, "fichero.json")

if __name__ == "__main__":


    try:
        fichSmil = sys.argv[1]
        my_Karaoke = KaraokeLocal(fichSmil)
        print(my_Karaoke)
        my_Karaoke.to_json(fichSmil)
        print(my_Karaoke)
        my_Karaoke.do_local()
        print(my_Karaoke)
        my_Karaoke.to_json(fichSmil)
        print(my_Karaoke)
    except IndexError:
        print("Usage: python3 karaoke.py file.smil")
