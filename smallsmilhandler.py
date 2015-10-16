
#author>> Roberto Yubero
#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from xml.sax.handler import ContentHandler
from xml.sax import make_parser


class SmallSMILHandler(ContentHandler):

    def __init__ (self):

        self.tags = []
        self.dic = {
        "root-layout": ['width', 'heigh', 'background-color'],
        "region": ['id', 'top', 'bottom', 'left', 'right'],
        "img": ['src', 'region', 'begin', 'dur'],
        "audio": ['src', 'begin', 'dur'],
        "textstream": ['src', 'region']
        }


    def startElement(self, name, attrs):
        """
        Metodo que se llama cuando se abre una etiqueta
        """
        if name in self.dic:
            dicc = {}
            for item in self.dic[name]:
                dicc[item] = attrs.get(item, "")
            self.tags.append([name, dicc])


if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    smilHandler = SmallSMILHandler()
    parser.setContentHandler(smilHandler)
    parser.parse(open('karaoke.smil'))
    print(smilHandler.tags)

    print(smilHandler.tags)
