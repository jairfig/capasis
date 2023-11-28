# Generated by Django 4.2.7 on 2023-11-28 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AulaAgendada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('hora_inicio', models.TimeField(blank=True, null=True)),
                ('hora_fim', models.TimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Aula',
            },
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True, max_length=255, null=True)),
                ('trilha', models.CharField(choices=[('IA', 'Inteligência Artificial'), ('IOT', 'Internet das Coisas'), ('MA', 'Manufatura Aditiva')], max_length=3)),
            ],
            options={
                'verbose_name': 'Módulo',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=255)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Professores',
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_turma', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Identificação da Turma')),
                ('data_matricula', models.DateTimeField(auto_now_add=True)),
                ('alunos', models.ManyToManyField(to='diario.aluno', verbose_name='Matriculados')),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diario.modulo')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diario.professor')),
            ],
        ),
        migrations.CreateModel(
            name='Presenca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situacao', models.CharField(blank=True, choices=[('P', 'Presente'), ('F', 'Faltou'), ('J', 'Justificada')], max_length=1, null=True)),
                ('justificativa', models.CharField(blank=True, max_length=255, null=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diario.aluno')),
                ('aula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diario.aulaagendada')),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conceito', models.CharField(choices=[('0', 'Insuficiente'), ('1', 'Regular'), ('2', 'Bom'), ('3', 'Excelente')], max_length=3)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diario.aluno')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diario.turma')),
            ],
        ),
        migrations.AddField(
            model_name='aulaagendada',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diario.turma'),
        ),
    ]
