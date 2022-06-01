import json
from pathlib import Path

class ObjectEncoder(object):
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if class_name == 'Lista':
                aparatos = d['Aparato']
                dAparatos = aparatos[0]
                lista = class_()
                for i in range(len(aparatos)):
                    dAparatos = aparatos[i]
                    class_name = dAparatos.pop('__class__')
                    class_ = eval(class_name)
                    atributos = dAparatos['__atributos__']
                    unAparato = class_(**atributos)
                    lista.agregarElemento(unAparato)
                return lista

    def leerJSONArchivo(self):
        with Path('aparatoselectronicos.json').open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario
       