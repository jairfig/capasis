from django.db import models

# Create your models here.
class Professor(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    email = models.CharField(max_length=255, null=False, blank=False)
    telefone = models.CharField(max_length=255, null=False, blank=False)
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    email = models.CharField(max_length=255, null=False, blank=False)
    telefone = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.nome


class Modulo(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    descricao = models.CharField(max_length=255, null=False, blank=False)
    trilha = models.CharField(max_length=3, choice=[('IA', 'Inteligência Artificial'),('IOT', 'Internet das Coisas'),('MA', 'Manufatura Aditiva')] , null=False, blank=False)

    def __str__(self):
        return self.nome


class Turma(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    alunos = models.ManyToManyField(Aluno)
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Aula(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    data = models.DateField(null=False, blank=False)
    hora_inicio = models.TimeField(null=True, blank=True)
    hora_fim = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.turma.modulos.nome + ' - ' + self.turma.nome + ' - ' + self.data.strftime('%d/%m/%Y')


class Presenca(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    presenca = models.BooleanField(null=False, blank=False)
    justificativa = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.aluno + ' - ' + self.aula.turma.nome + ' - ' + self.aula.data.strftime('%d/%m/%Y') + ' - ' + self.presenca


class Avaliacao(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    conceito = models.CharField(max_length=3, choice=[('0', 'Insuficiente'), ('1', 'Regular'),
                                                    ('2', 'Bom'), ('3', 'Excelente')], null=False, blank=False)

    def __str__(self):
        return f"{self.aluno} - {self.turma} - Nota: {self.conceito}"


