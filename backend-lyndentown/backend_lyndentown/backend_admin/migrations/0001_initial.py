# Generated by Django 4.0.2 on 2022-03-11 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Minigame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_minigame', models.CharField(max_length=100)),
                ('nombre_objeto', models.CharField(max_length=100)),
                ('tasa', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Objects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_name', models.CharField(max_length=256)),
                ('object_weight', models.FloatField()),
                ('object_quantity', models.IntegerField()),
                ('object_posX', models.IntegerField()),
                ('object_posY', models.IntegerField()),
                ('object_order', models.IntegerField()),
                ('object_hardness', models.CharField(max_length=256)),
                ('object_color', models.CharField(blank=None, max_length=256)),
                ('object_quality', models.IntegerField()),
                ('object_level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ObjectsInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_quantity', models.IntegerField()),
                ('object_posX', models.IntegerField()),
                ('object_posY', models.IntegerField()),
                ('object_order', models.IntegerField()),
                ('object_quality', models.IntegerField()),
                ('object_level', models.IntegerField()),
                ('object_apilable', models.IntegerField()),
                ('object_equipable', models.IntegerField()),
                ('object_direccion', models.IntegerField()),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objects')),
            ],
        ),
        migrations.CreateModel(
            name='Personaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('energia', models.IntegerField()),
                ('hambre', models.IntegerField()),
                ('calor', models.IntegerField()),
                ('higiene', models.IntegerField()),
                ('felicidad', models.IntegerField()),
                ('salud', models.IntegerField()),
                ('fuerza', models.IntegerField()),
                ('inteligencia', models.IntegerField()),
                ('carisma', models.IntegerField()),
                ('suerte', models.IntegerField()),
                ('greenleaves', models.IntegerField()),
                ('habilidades', models.CharField(max_length=20)),
                ('profesiones', models.CharField(max_length=20)),
                ('atuendos', models.CharField(default='No hay atuendos', max_length=20)),
                ('eth', models.IntegerField()),
                ('seccion_id', models.IntegerField()),
                ('posX', models.IntegerField()),
                ('posY', models.IntegerField()),
                ('inventario', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('valor', models.IntegerField(default=0)),
                ('tipo', models.IntegerField()),
                ('nombre_pj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_admin.personaje')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion39',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=39)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion38',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=38)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion37',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=37)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion36',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=36)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion35',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=35)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion34',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=34)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion33',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=33)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion32',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=32)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion31',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=31)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion30',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=30)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion29',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=29)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion28',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=28)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion27',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=27)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion26',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=26)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion25',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=25)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion24',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=24)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion23',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=23)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion22',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=22)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion21',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=21)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion20',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=20)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion19',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=19)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion18',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=18)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion17',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=17)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion16',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=16)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion15',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=15)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion14',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=14)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion13',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=13)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion12',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=12)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion11',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=11)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion10',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=10)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion09',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=9)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion08',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=8)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion07',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=7)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion06',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=6)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion05',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=5)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion04',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=4)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion03',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=3)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion02',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=2)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion01',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seccion', models.IntegerField(default=1)),
                ('objectsinstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
                ('id_pj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_admin.personaje')),
            ],
        ),
        migrations.CreateModel(
            name='Highscore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('id_pj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_admin.personaje')),
                ('nombre_minigame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_admin.minigame')),
            ],
        ),
        migrations.CreateModel(
            name='Atuendo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_admin.objectsinstance')),
                ('id_pj', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend_admin.personaje')),
            ],
        ),
    ]
