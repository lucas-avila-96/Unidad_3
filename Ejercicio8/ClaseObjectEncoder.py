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
                personas = d['Personal']
                dPersonas = personas[0]
                lista = class_()
                for i in range(len(personas)):
                    dPersonas = personas[i]
                    class_name = dPersonas.pop('__class__')
                    class_ = eval(class_name)
                    atributos = dPersonas['__atributos__']
                    unaPersona = class_(**atributos)
                    lista.agregarItem(unaPersona)
                return lista

    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario
       