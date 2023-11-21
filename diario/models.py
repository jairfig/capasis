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
    descricao = models.TextField(max_length=255, null=True, blank=True)
    trilha = models.CharField(max_length=3, choices=[('IA', 'Inteligência Artificial'),('IOT', 'Internet das Coisas'),('MA', 'Manufatura Aditiva')] , null=False, blank=False)

    def __str__(self):
        return self.nome


class Turma(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    alunos = models.ManyToManyField(Aluno)

    def __str__(self):
        return self.nome


class AulaAgendada(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    data = models.DateField(null=False, blank=False)
    hora_inicio = models.TimeField(null=True, blank=True)
    hora_fim = models.TimeField(null=True, blank=True)

    def get_alunos_matriculados(self):
        return self.turma.alunos.all()

    def __str__(self):
        return self.turma.modulo.nome + ' - ' + self.data.strftime('%d/%m/%Y')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        alunos_turma = self.turma.alunos.all()
        for aluno in alunos_turma:
            Presenca.objects.create(aula=self, aluno=aluno)

# @receiver(post_save, sender=AulaAgendada)
# def criar_presencas(sender, instance, **kwargs):
#     # Verifique se a aula foi recém-criada para evitar chamadas desnecessárias
#     if kwargs.get('created', False):
#         # Obtenha todos os alunos da turma
#         alunos_turma = instance.turma.alunos.all()
#         # Crie instâncias de Presenca para cada aluno da turma
#         for aluno in alunos_turma:
#             Presenca.objects.create(aula=instance, aluno=aluno)


class Presenca(models.Model):
    aula = models.ForeignKey(AulaAgendada, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    situacao = models.CharField(max_length=1, choices=[('P', 'Presente'), ('F', 'Faltou'),
                                                       ('J', 'Justificada')], null=True, blank=True)
    justificativa = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.aluno.nome + ' - ' + self.aula.turma.nome + ' - ' + self.aula.data.strftime('%d/%m/%Y')


class Avaliacao(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    conceito = models.CharField(max_length=3, choices=[('0', 'Insuficiente'), ('1', 'Regular'),
                                                    ('2', 'Bom'), ('3', 'Excelente')], null=False, blank=False)

    def __str__(self):
        return f"{self.aluno} - {self.turma} - Nota: {self.conceito}"


