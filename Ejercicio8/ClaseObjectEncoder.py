import json
from pathlib import Path
from ClaseLista import Lista
from ClaseDocenteInvestigador import DocenteInvestigador
from ClaseInvestigador import Investigador
from ClaseDocente import Docente
from ClasePersonalApoyo import PersonalApoyo


class ObjectEncoder(object):
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if class_name == 'Lista':
                agentes = d['agentes']
                dAgente = agentes[0]
                lista = class_()
                for i in range(len(agentes)):
                    dAgente = agentes[i]
                    class_name = dAgente.pop('__class__')
                    class_ = eval(class_name)
                    atributos = dAgente['__atributos__']
                    unAgente = class_(**atributos)
                    lista.agregarElemento(unAgente)
            return lista

    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario
            
    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close() 