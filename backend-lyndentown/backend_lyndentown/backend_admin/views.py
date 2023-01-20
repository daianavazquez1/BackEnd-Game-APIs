from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *

# API GET PARA TRAER TODOS LOS DATOS DEL PERSONAJE PASANDO SU ID POR URL
class PersonajeAPI(APIView):
    def get(self, request, nombre):
        personaje = Personaje.objects.filter(id=nombre).first()

        a = []
        inv = Inventory.objects.filter(id_pj=nombre)
        if len(inv) == 0:
            ids = "[El personaje no tiene ningun objeto.]"
        else:
            for i in Inventory.objects.filter(id_pj=nombre):
                e = i.id
                a.append(e)
                ids = str(a)


        params={'nombre': personaje.nombre, 'energia': personaje.energia, 'hambre': personaje.hambre, 'calor': personaje.calor,
                'higiene': personaje.higiene, 'felicidad': personaje.felicidad, 'salud': personaje.salud, 'fuerza': personaje.fuerza,
                'inteligencia': personaje.inteligencia, 'carisma': personaje.carisma, 'suerte': personaje.suerte,
                'greenleaves': personaje.greenleaves, 'habilidades': personaje.habilidades, 'profesiones': personaje.profesiones,
                'eth': personaje.eth, 'seccion_id': personaje.seccion_id, 'posX': personaje.posX,
                'posY': personaje.posY, 'inventario': ids[1:-1]}
        data = {'Personaje': params}
        return Response(data)

"""APIS CREADAS POR DAIANA CAROLINA VAZQUEZ"""
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------

class SeccionAPI(APIView):
    def get(self, request, seccionid):
        seccion= []
        if seccionid == 1:
            seccion = Seccion01.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 2:
            seccion = Seccion02.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 3:
            seccion = Seccion03.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 4:
            seccion = Seccion04.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 5:
            seccion = Seccion05.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 6:
            seccion = Seccion06.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 7:
            seccion = Seccion07.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 8:
            seccion = Seccion08.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 9:
            seccion = Seccion09.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 10:
            seccion = Seccion10.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 11:
            seccion = Seccion11.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 12:
            seccion = Seccion12.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 13:
            seccion = Seccion13.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 14:
            seccion = Seccion14.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 15:
            seccion = Seccion15.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 16:
            seccion = Seccion16.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 17:
            seccion = Seccion17.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 18:
            seccion = Seccion18.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 19:
            seccion = Seccion19.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 20:
            seccion = Seccion20.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 21:
            seccion = Seccion21.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 22:
            seccion = Seccion22.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 23:
            seccion = Seccion23.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 24:
            seccion = Seccion24.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 25:
            seccion = Seccion25.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 26:
            seccion = Seccion26.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 27:
            seccion = Seccion27.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 28:
            seccion = Seccion28.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 29:
            seccion = Seccion29.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 30:
            seccion = Seccion30.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 31:
            seccion = Seccion31.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 32:
            seccion = Seccion32.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 33:
            seccion = Seccion33.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 34:
            seccion = Seccion34.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 35:
            seccion = Seccion35.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 36:
            seccion = Seccion36.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 37:
            seccion = Seccion37.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 38:
            seccion = Seccion38.objects.filter(id_seccion=int(seccionid)).all()
        elif seccionid == 39:
            seccion = Seccion39.objects.filter(id_seccion=int(seccionid)).all()

        lista_de_salida = []
        for dato in seccion:
            diccionario = {}
            diccionario["id_seccion"] = dato.id_seccion
            diccionario["id_instacia"] = dato.objectsinstance.id
            diccionario["posx"] = dato.objectsinstance.object_posX
            diccionario["posy"] = dato.objectsinstance.object_posY
            diccionario["order"] = dato.objectsinstance.object_order
            diccionario["level"] = dato.objectsinstance.object_level
            diccionario["queality"] = dato.objectsinstance.object_quality
            diccionario["quantity"] = dato.objectsinstance.object_quantity
            diccionario["weight"] = dato.objectsinstance.object.object_weight
            diccionario["name"] = dato.objectsinstance.object.object_name
            diccionario["hardness"] = dato.objectsinstance.object.object_hardness
            diccionario["color"] = dato.objectsinstance.object.object_color
            lista_de_salida.append(diccionario)

        info_de_seccion = {'info_seccion': lista_de_salida}
        return Response(info_de_seccion)


class MinigameAPI(APIView):
    def post(self, request):
        try:
            minigame = Minigame.objects.get(nombre_minigame=request.data.get("nombre_minigame"))
            score_minigame = int(request.data.get("score"))

            objects = Objects.objects.get(object_name=minigame.nombre_objeto)

            instancia_objeto = ObjectsInstance()
            instancia_objeto.object_quantity = int(score_minigame) // int(minigame.tasa)
            instancia_objeto.object_quality = objects.object_quality
            instancia_objeto.object_level = objects.object_level
            instancia_objeto.object_order = objects.object_order
            instancia_objeto.object_posY = objects.object_posY
            instancia_objeto.object_posX = objects.object_posX
            instancia_objeto.object_apilable = 0
            instancia_objeto.object_equipable = 0
            instancia_objeto.object_direccion = 0
            instancia_objeto.object = objects
            instancia_objeto.save()

            nuevo_inventory = Inventory()

            nuevo_inventory.id_object = instancia_objeto
            nuevo_inventory.id_pj = Personaje.objects.get(nombre=request.data.get("nombre"))
            nuevo_inventory.save()

            return Response(True)
        except Exception:
            return Response(False)

class HighscoresAPI(APIView):
    def post(self, request):
        try:
            nuevo = Highscore()
            nuevo.nombre_minigame = Minigame.objects.get(nombre_minigame=request.data.get("nombre_minigame"))
            nuevo.id_pj = Personaje.objects.get(nombre=request.data.get("nombre"))
            nuevo.score = request.data.get("score")

            comprobacion = Highscore.objects.filter(id_pj=nuevo.id_pj, nombre_minigame=nuevo.nombre_minigame).first()
            if comprobacion:
                if nuevo.score > comprobacion.score and nuevo.nombre_minigame == comprobacion.nombre_minigame:
                    comprobacion.score = nuevo.score
                    comprobacion.save()
                else:
                    pass
            else:
                nuevo.save()

            return Response(True)
        except Exception as e:
            return Response(e)

class HighscoresAPI(APIView):
    def post(self, request):
        try:
            nuevo = Highscore()
            nuevo.nombre_minigame = Minigame.objects.get(nombre_minigame=request.data.get("nombre_minigame"))
            nuevo.id_pj = Personaje.objects.get(nombre=request.data.get("nombre"))
            nuevo.score = request.data.get("score")

            comprobacion = Highscore.objects.filter(id_pj=nuevo.id_pj, nombre_minigame=nuevo.nombre_minigame).first()
            if comprobacion:
                if nuevo.score > comprobacion.score and nuevo.nombre_minigame == comprobacion.nombre_minigame:
                    comprobacion.score = nuevo.score
                    comprobacion.save()
                else:
                    pass
            else:
                nuevo.save()

            return Response(True)
        except Exception:
            return Response(False)

class GettransaccionesAPI(APIView):
    def get(self, request, personaje, tipo):
        try:
            #0=compra, 1=venta, 2=compra y venta(todas las operaciones)
            pers = Personaje.objects.filter(nombre=personaje).first()
            pj = []
            tip = []

            if "mercado" == personaje and tipo == 0:
                todo = Transaccion.objects.filter(tipo=0).all()
                lista_de_salida = []
                for dato in todo:
                    diccionario = {}
                    diccionario["id de transaccion"] = dato.id
                    diccionario["nombre_pj"] = dato.nombre_pj.nombre
                    diccionario["fecha"] = dato.fecha
                    diccionario["valor"] = dato.valor
                    diccionario["tipo"] = dato.tipo
                    lista_de_salida.append(diccionario)

                info = {'info': lista_de_salida}
                return Response(info)

            elif "mercado" == personaje and tipo == 1:
                todo = Transaccion.objects.filter(tipo=1).all()
                lista_de_salida = []
                for dato in todo:
                    diccionario = {}
                    diccionario["id de transaccion"] = dato.id
                    diccionario["nombre_pj"] = dato.nombre_pj.nombre
                    diccionario["fecha"] = dato.fecha
                    diccionario["valor"] = dato.valor
                    diccionario["tipo"] = dato.tipo
                    lista_de_salida.append(diccionario)

                info = {'info': lista_de_salida}
                return Response(info)

            elif "mercado" == personaje and tipo == 2:
                todo = Transaccion.objects.all()
                lista_de_salida = []
                for dato in todo:
                    diccionario = {}
                    diccionario["id de transaccion"] = dato.id
                    diccionario["nombre_pj"] = dato.nombre_pj.nombre
                    diccionario["fecha"] = dato.fecha
                    diccionario["valor"] = dato.valor
                    diccionario["tipo"] = dato.tipo
                    lista_de_salida.append(diccionario)

                info = {'info': lista_de_salida}
                return Response(info)


            elif pers.nombre == personaje:
                if tipo == 0:
                    tip = Transaccion.objects.filter(nombre_pj=pers, tipo=tipo).all()
                    lista_de_salida = []
                    for dato in tip:
                        diccionario = {}
                        diccionario["id de transaccion"] = dato.id
                        diccionario["nombre_pj"] = dato.nombre_pj.nombre
                        diccionario["fecha"] = dato.fecha
                        diccionario["valor"] = dato.valor
                        diccionario["tipo"] = tipo
                        lista_de_salida.append(diccionario)
                    info = {'info': lista_de_salida}
                    return Response(info)

                elif tipo == 1:
                    tip = Transaccion.objects.filter(nombre_pj=pers,tipo=tipo).all()
                    lista_de_salida = []
                    for dato in tip:
                        diccionario = {}
                        diccionario["id de transaccion"] = dato.id
                        diccionario["nombre_pj"] = dato.nombre_pj.nombre
                        diccionario["fecha"] = dato.fecha
                        diccionario["valor"] = dato.valor
                        diccionario["tipo"] = dato.tipo
                        lista_de_salida.append(diccionario)
                    info = {'info': lista_de_salida}
                    return Response(info)

                elif tipo == 2:
                    pj = Transaccion.objects.filter(nombre_pj=pers).all()
                    lista_de_salida = []
                    for dato in pj:
                        diccionario = {}
                        diccionario["id de transaccion"] = dato.id
                        diccionario["nombre_pj"] = dato.nombre_pj.nombre
                        diccionario["fecha"] = dato.fecha
                        diccionario["valor"] = dato.valor
                        diccionario["tipo"] = dato.tipo
                        lista_de_salida.append(diccionario)
                    info = {'info': lista_de_salida}
                    return Response(info)

        except Exception:
            return Response(False)

#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------

class ObjectsInstanceAPI(APIView):
    def post(self, request):
        data = {"objeto":True}
        try:
            otro_objeto = Objects.objects.filter(id=request.data["otro_objeto"]).first()
            nuevo_objeto = ObjectsInstance()
            nuevo_objeto.object_order = request.data.get("order")
            nuevo_objeto.object_level = request.data.get("level")
            nuevo_objeto.object_quality = request.data.get("quality")
            nuevo_objeto.object_quantity = request.data.get("quantity")
            nuevo_objeto.object_posY = request.data.get("pos_y")
            nuevo_objeto.object_posX = request.data.get("pos_x")
            nuevo_objeto.object_apilable = request.data.get("apilable")
            nuevo_objeto.object_equipable = request.data.get("equipable")
            nuevo_objeto.object_direccion = request.data.get("direccion")
            nuevo_objeto.object = otro_objeto
            nuevo_objeto.save()
        except Exception as i:
            data = {"objeto":i}
        return Response(data)

class PersonajeSpawnAPI(APIView):
    def post(self, request):
        data = {"pj": True}
        try:
            personaje = Personaje.objects.filter(nombre=request.data["personaje"]).first()
            personaje.seccion_id = request.data.get("seccion_id")
            personaje.posX = request.data.get("posX")
            personaje.posY = request.data.get("posY")
            personaje.save()
        except Exception as i:
            data = {"pj":i}
        return Response(data)

class InventarioAPI(APIView):
    def get(self, request, id_pj):
        data = {}
        objetos = Inventory.objects.filter(id_pj=id_pj).all()
        for objeto in objetos:
            data[objeto.id_objeto] = objeto
            print(data[objeto.id_objeto])
        return Response(data)

class Posicion_pjAPI(APIView):
    def post(self,request):
        data = {'respuesta':True}
        try:
            personaje = Personaje.objects.get(nombre=request.data.get('nombre'))
            personaje.posX = request.data.get("posX")
            personaje.posY = request.data.get('posY')
            personaje.save()
        except Exception as e:
            data = {"respuesta":e}
        return Response(data)

class PosttrasaccionesAPI(APIView):
    def post(self, request):
        try:
            transaccion = Transaccion()
            transaccion.nombre_pj= Personaje.objects.get(nombre=request.data.get("nombre"))
            transaccion.valor = request.data.get("valor")
            transaccion.tipo = request.data.get("tipo")
            transaccion.save()
            return Response(True)

        except Exception:
            return Response(False)
#Tipo de transaccion: 1 para compra, 0 para venta.

# API PARA AGREGAR EL ID DE LOS OBJECTOS DE INSTANCIA A LA TABLA INVENTORY CON EL NOMBRE DE UN PERSONAJE
# LA PETICION ESPERA UN DICCIONARIO COMO ESTE: {"id_pj" : "pepe", "id" : <ID DEL OBJETO>}

class TablaInventarioAPI(APIView):
    def post(self, request):
        try:
            pj = request.data.get('id_pj')
            nuevo_inventario = Inventory()
            nuevo_inventario.id_pj = Personaje.objects.filter(nombre=pj).first()
            nuevo_inventario.id_object = ObjectsInstance.objects.filter(id=int(request.data.get("id"))).first()
            nuevo_inventario.save()

            return Response(True)
        except Exception:
            return Response(False)


# API PARA ACTUALIZAR UNA STAT DEL PERSONAJE. REQUIERE UN DICCIONARIO COMO ESTE:
# {"nombre" : "pepe", "stat" : "salud", "valor" : 10}

class Stats_PersonajeAPI(APIView):
    def post(self, request):
        try:
            personaje = Personaje.objects.filter(nombre=request.data.get("nombre")).first()
            stat = request.data.get("stat")
            valor = request.data.get("valor")
            if stat == "energia":
                personaje.energia = valor
            elif stat == "hambre":
                personaje.hambre = valor
            elif stat == "calor":
                personaje.calor = valor
            elif stat == "higiene":
                personaje.higiene = valor
            elif stat == "felicidad":
                personaje.felicidad = valor
            elif stat == "salud":
                personaje.salud = valor
            elif stat == "fuerza":
                personaje.fuerza = valor
            elif stat == "inteligencia":
                personaje.inteligencia = valor
            elif stat == "carisma":
                personaje.carisma = valor
            elif stat == "suerte":
                personaje.suerte = valor

            personaje.save()

            return Response(True)
        except Exception:
            return Response(False)

# API GET PARA TRAER LOS ATUENDOS DEL PERSONAJE PASANDO SU NOMBRE POR URL
class AtuendosAPI(APIView):
    def get(self, request, nombre):
        try:
            personaje = Personaje.objects.filter(nombre=nombre).first()

            lista_atuendos = []
            inv_atuendos = Atuendo.objects.filter(id_pj=personaje)
            if len(inv_atuendos) == 0:
                ids_atuendos = "[El personaje no posee ningun atuendo]"
            else:
                for i in Atuendo.objects.filter(id_pj=personaje):
                    e = i.id
                    lista_atuendos.append(e)
                    ids_atuendos = str(lista_atuendos)

            params = {'id_pj': personaje.id, 'atuendo': ids_atuendos[1:-1]}

            return Response(params)
        except Exception:
            return Response(False)

class GetObjectInstances(APIView):
    def get(self, request, ids):
        data = []
        lista_ids = ids.split(",")
        for id in lista_ids:
            try:
                objectsInstance = ObjectsInstance.objects.get(id=id)
                dict = {}
                dict["object_quantity"] = objectsInstance.object_quantity
                dict["object_posX"] = objectsInstance.object_posX
                dict["object_posY"] = objectsInstance.object_posY
                dict["object_order"] = objectsInstance.object_order
                dict["object_quality"] = objectsInstance.object_quality
                dict["object_level"] = objectsInstance.object_level
                dict["weight"] = objectsInstance.object.object_weight
                dict["name"] = objectsInstance.object.object_name
                dict["hardness"] = objectsInstance.object.object_hardness
                dict["color"] = objectsInstance.object.object_color
                dict_dos = {id : dict}
                data.append(dict_dos)
            except Exception as e:
                print(e)
        return Response({"data": data})

