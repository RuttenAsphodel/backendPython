# Generated by Django 4.1.8 on 2023-06-12 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contratosEquipos',
            fields=[
                ('serie', models.CharField(default='MXL9123KS1', max_length=30, primary_key=True, serialize=False, verbose_name='Serie')),
                ('ubicacion', models.CharField(default='Corte De Apelaciones De Arica', max_length=100, verbose_name='Ubicacion')),
                ('tipo_equipo', models.CharField(default='Computador', max_length=40, verbose_name='Tipo')),
                ('marca_modelo', models.CharField(default='Hp - Prodesk 600g4', max_length=40, verbose_name='Modelo')),
                ('contrato', models.CharField(default='Pjud4_Anexo3', max_length=14, verbose_name='Contrato')),
            ],
        ),
        migrations.CreateModel(
            name='equiposSpare',
            fields=[
                ('folioTicket', models.IntegerField(default='654321', primary_key=True, serialize=False, verbose_name='Folio')),
                ('estado', models.CharField(default='Pendiente Retiro', max_length=20, verbose_name='Estado')),
                ('tipo', models.CharField(default='PC', max_length=12, verbose_name='Tipo')),
                ('serie', models.CharField(default='MXL9123KS1', max_length=25, verbose_name='Serie')),
                ('modelo', models.CharField(default='HP Prodesk 600 G4', max_length=30, verbose_name='Modelo')),
                ('fechaRetiro', models.DateField(blank=True, default='2023-06-10')),
                ('transporte', models.CharField(max_length=25, null=True, verbose_name='Transporte')),
                ('observaciones', models.CharField(default='Pendiente Despacho', max_length=40, verbose_name='Observaciones')),
            ],
        ),
        migrations.CreateModel(
            name='especialistas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTecnico', models.CharField(default='John Doe', max_length=50, verbose_name='Nombre Tecnico')),
                ('residenciaTecnico', models.CharField(default='CAPJ', max_length=30, verbose_name='Residencia')),
            ],
        ),
        migrations.CreateModel(
            name='modeloEquipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modeloEquipo', models.CharField(max_length=100, verbose_name='Modelo')),
            ],
        ),
        migrations.CreateModel(
            name='proyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProyecto', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='soluciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcionCorta', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tecnicoResidente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('runTecnico', models.CharField(default='12345678-9', max_length=13, verbose_name='Rut Tecnico')),
                ('nombreTecnico', models.CharField(default='John Doe', max_length=50, verbose_name='Nombre Tecnico')),
                ('residenciaTecnico', models.CharField(default='CAPJ', max_length=30, verbose_name='Residencia')),
            ],
        ),
        migrations.CreateModel(
            name='ubicaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.CharField(max_length=100, verbose_name='Ubicacion')),
            ],
        ),
        migrations.CreateModel(
            name='ordenes',
            fields=[
                ('folioTicket', models.IntegerField(default='5422590', primary_key=True, serialize=False, verbose_name='Folio Ticket')),
                ('fechaSolicitud', models.DateField(default='20-04-2020', verbose_name='Fecha Solicitud')),
                ('horaSolicitud', models.TimeField(default='11:39:00', verbose_name='Hora Solicitud')),
                ('nombreSolicitante', models.CharField(default='Carlos Boza', max_length=100, verbose_name='Nombre Solicitante')),
                ('telefono', models.IntegerField(default='229759700', null=True, verbose_name='Telefono')),
                ('email', models.EmailField(default='cboza@pjud.cl', max_length=254, verbose_name='Email')),
                ('direccion', models.CharField(blank=True, default='direccion', max_length=100)),
                ('serieReportada', models.CharField(max_length=50, verbose_name='Serie Reportada')),
                ('ipReportada', models.CharField(max_length=20, verbose_name='IP Reportada')),
                ('fechaSoporte', models.DateField(blank=True, default='20-04-2020', verbose_name='Fecha Soporte')),
                ('horaSoporte', models.TimeField(blank=True, default='13:00:00', verbose_name='Hora Soporte')),
                ('descripcionSoporte', models.TextField(blank=True, max_length=100, verbose_name='Descripcion Soporte')),
                ('solucionDetalle', models.TextField(blank=True, max_length=100, verbose_name='Solucion Detallada')),
                ('fechaTermino', models.DateField(blank=True, default='20-04-2020', verbose_name='Fecha Termino')),
                ('horaTermino', models.TimeField(blank=True, default='15:00:00', verbose_name='Hora Termino')),
                ('responsable', models.CharField(blank=True, default='Responsable', max_length=50, verbose_name='Responsable')),
                ('orden_docum', models.FileField(blank=True, upload_to='', verbose_name='Orden de Trabajo')),
                ('contratoReportado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.proyectos')),
                ('id_equipoReportado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.modeloequipos')),
                ('id_especialista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.especialistas')),
                ('id_solucionCorta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.soluciones')),
                ('id_ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.ubicaciones')),
            ],
        ),
    ]
