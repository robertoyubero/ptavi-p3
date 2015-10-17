#author>> Roberto Yubero
#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler
import sys
import urllib

class Karaoke():

    def print_tags(self, list_tags):
        #1-busco etiqueta
        #2-compruebo que los atributos no esten vacios
            #2a-no esta vacia >> imprimo
            #2b-esta vacia >> paso a la  siguiente etiqueta
        for elemento in list_tags:
            etiqueta = elemento[0]
            diccionario = elemento[1]
            mis_atributos = ""

            for atributo in diccionario.keys():
                if diccionario[atributo] != "":
                    mis_atributos += "\t" + atributo + '="' + diccionario[atributo] + '"'
            print(etiqueta + mis_atributos + "\n")

if __name__ == "__main__":


    parser = make_parser()
    smilHandler = SmallSMILHandler()
    parser.setContentHandler(smilHandler)
    try:
        parser.parse(open(sys.argv[1], 'r'))
        my_tags = smilHandler.get_tags()
        karaokeHandler = Karaoke()
        karaokeHandler.print_tags(my_tags)
    except IndexError:
        print("Usage: python3 karaoke.py file.smil")
