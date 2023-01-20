from django.db import models

#caracteristicas propias
class Objects(models.Model):
    object_name = models.CharField(max_length=256, blank=False, null=False)
    object_weight = models.FloatField(blank=False, null=False)
    object_quantity = models.IntegerField(blank=False, null=False)
    object_posX = models.IntegerField(blank=False, null=False)
    object_posY = models.IntegerField(blank=False, null=False)
    object_order = models.IntegerField(blank=False, null=False)
    object_hardness = models.CharField(max_length=256, blank=False, null=False)
    object_color = models.CharField(max_length=256, blank=None, null=False)
    object_quality = models.IntegerField(blank=False, null=False)
    object_level = models.IntegerField(blank=False, null=False)


#caracteristicas modificables
class ObjectsInstance(models.Model):
    object_quantity = models.IntegerField(blank=False, null=False)
    object_posX = models.IntegerField(blank=False, null=False)
    object_posY = models.IntegerField(blank=False, null=False)
    object_order = models.IntegerField(blank=False, null=False)
    object_quality = models.IntegerField(blank=False, null=False)
    object_level = models.IntegerField(blank=False, null=False)
    object_apilable = models.IntegerField(blank=False, null=False)
    object_equipable = models.IntegerField(blank=False, null=False)
    object_direccion = models.IntegerField(blank=False, null=False)
    object = models.ForeignKey(Objects, on_delete=models.CASCADE)


class Personaje(models.Model):
    nombre = models.CharField(max_length=15, blank=False, null=False)
    energia = models.IntegerField(blank=False, null=False)
    hambre = models.IntegerField(blank=False, null=False)
    calor = models.IntegerField(blank=False, null=False)
    higiene = models.IntegerField(blank=False, null=False)
    felicidad = models.IntegerField(blank=False, null=False)
    salud = models.IntegerField(blank=False, null=False)
    fuerza = models.IntegerField(blank=False, null=False)
    inteligencia = models.IntegerField(blank=False, null=False)
    carisma = models.IntegerField(blank=False, null=False)
    suerte = models.IntegerField(blank=False, null=False)
    greenleaves = models.IntegerField(blank=False, null=False)
    habilidades = models.CharField(max_length=20, blank=False, null=False)
    profesiones = models.CharField(max_length=20, blank=False, null=False)
    atuendos = models.CharField(max_length=20, blank=False, null=False, default='No hay atuendos')
    eth = models.IntegerField(blank=False, null=False)
    seccion_id = models.IntegerField(blank=False, null=False)
    posX = models.IntegerField(blank=False, null=False)
    posY = models.IntegerField(blank=False, null=False)
    inventario = models.CharField(max_length=300, blank=True, null=False)


class Inventory(models.Model):
    id_pj = models.ForeignKey(Personaje, blank=False, null=False, on_delete=models.CASCADE)
    id_object = models.ForeignKey(ObjectsInstance, blank=False, null=False, on_delete=models.CASCADE)


class Atuendo(models.Model):
    id_pj = models.ForeignKey(Personaje, blank=True, null=False, on_delete=models.CASCADE)
    id_object = models.ForeignKey(ObjectsInstance, blank=False, null=False, on_delete=models.CASCADE)

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
"""CLASES CREADAS POR DAIANA CAROLINA VAZQUEZ"""

class Minigame(models.Model):
    nombre_minigame = models.CharField(max_length= 100, blank=False, null=False)
    nombre_objeto = models.CharField(max_length= 100, blank=False, null=False)
    tasa = models.IntegerField (blank=False, null=False)


class Highscore(models.Model):
    nombre_minigame = models.ForeignKey(Minigame, blank=False, null=False, on_delete=models.CASCADE)
    id_pj = models.ForeignKey(Personaje, blank=False, null=False, on_delete=models.CASCADE)
    score = models.IntegerField(blank=False, null=False, default=0)


class Transaccion(models.Model):
    fecha = models.DateField(auto_now_add=True, null=False, blank=False)
    nombre_pj = models.ForeignKey(Personaje, blank=False, null=False, on_delete=models.CASCADE)
    valor = models.IntegerField(blank=False, null=False, default=0)
    tipo = models.IntegerField(blank=False, null=False)


class Seccion01(models.Model):
    id_seccion = models.IntegerField(default=1)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion02(models.Model):
    id_seccion = models.IntegerField(default=2)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion03(models.Model):
    id_seccion = models.IntegerField(default=3)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion04(models.Model):
    id_seccion = models.IntegerField(default=4)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion05(models.Model):
    id_seccion = models.IntegerField(default=5)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion06(models.Model):
    id_seccion = models.IntegerField(default=6)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion07(models.Model):
    id_seccion = models.IntegerField(default=7)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion08(models.Model):
    id_seccion = models.IntegerField(default=8)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion09(models.Model):
    id_seccion = models.IntegerField(default=9)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion10(models.Model):
    id_seccion = models.IntegerField(default=10)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion11(models.Model):
    id_seccion = models.IntegerField(default=11)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion12(models.Model):
    id_seccion = models.IntegerField(default=12)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion13(models.Model):
    id_seccion = models.IntegerField(default=13)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion14(models.Model):
    id_seccion = models.IntegerField(default=14)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion15(models.Model):
    id_seccion = models.IntegerField(default=15)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion16(models.Model):
    id_seccion = models.IntegerField(default=16)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion17(models.Model):
    id_seccion = models.IntegerField(default=17)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion18(models.Model):
    id_seccion = models.IntegerField(default=18)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion19(models.Model):
    id_seccion = models.IntegerField(default=19)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion20(models.Model):
    id_seccion = models.IntegerField(default=20)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion21(models.Model):
    id_seccion = models.IntegerField(default=21)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion22(models.Model):
    id_seccion = models.IntegerField(default=22)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion23(models.Model):
    id_seccion = models.IntegerField(default=23)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion24(models.Model):
    id_seccion = models.IntegerField(default=24)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion25(models.Model):
    id_seccion = models.IntegerField(default=25)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion26(models.Model):
    id_seccion = models.IntegerField(default=26)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion27(models.Model):
    id_seccion = models.IntegerField(default=27)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion28(models.Model):
    id_seccion = models.IntegerField(default=28)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion29(models.Model):
    id_seccion = models.IntegerField(default=29)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion30(models.Model):
    id_seccion = models.IntegerField(default=30)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion31(models.Model):
    id_seccion = models.IntegerField(default=31)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion32(models.Model):
    id_seccion = models.IntegerField(default=32)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion33(models.Model):
    id_seccion = models.IntegerField(default=33)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion34(models.Model):
    id_seccion = models.IntegerField(default=34)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion35(models.Model):
    id_seccion = models.IntegerField(default=35)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion36(models.Model):
    id_seccion = models.IntegerField(default=36)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion37(models.Model):
    id_seccion = models.IntegerField(default=37)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion38(models.Model):
    id_seccion = models.IntegerField(default=38)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)


class Seccion39(models.Model):
    id_seccion = models.IntegerField(default=39)
    objectsinstance = models.ForeignKey(ObjectsInstance, null=True, on_delete=models.CASCADE)
