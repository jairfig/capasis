from django.db import models
from django.utils import timezone
# from autoslug import AutoSlugField


# Create your models here.
class Professor(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    email = models.CharField(max_length=255, null=False, blank=False)
    telefone = models.CharField(max_length=255, null=False, blank=False)
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Professores"


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

    class Meta:
        verbose_name = "Módulo"


class Turma(models.Model):
    # nome_turma = AutoSlugField(populate_from=('modulo', 'professor'), unique=True)
    nome_turma = models.CharField('Identificação da Turma', max_length=255, unique=True, blank=True, null=True)
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    alunos = models.ManyToManyField(Aluno, verbose_name="Matriculados")
    data_matricula = models.DateTimeField(auto_now_add=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.nome_turma:
            today = timezone.now()
            year_month = today.strftime('%Y-%m')
            self.nome_turma = f"{year_month}-{self.modulo}-{self.professor}"
        super().save(*args, **kwargs)

    def percentual_decorrido(self):
        total = self.aula_set.count()
        decorrido = self.aula_set.filter(data__lte=timezone.now()).count()

        return int((decorrido / total) * 100 if total > 0 else 0)

    def __str__(self):
        return self.nome_turma


class Aula(models.Model):
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

    class Meta:
        verbose_name = "Aula"


class Presenca(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    presente = models.BooleanField(default=False, null=True, blank=False)
    justificativa = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.aluno.nome + ' - ' + self.aula.turma.nome_turma + ' - ' + self.aula.data.strftime('%d/%m/%Y')


class Avaliacao(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    conceito = models.CharField(max_length=3, choices=[('0', 'Insuficiente'), ('1', 'Regular'),
                                                    ('2', 'Bom'), ('3', 'Excelente')], null=False, blank=False)

    def __str__(self):
        return f"{self.aluno} - {self.turma} - Nota: {self.conceito}"


