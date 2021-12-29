from django.db import models
from Shartnoma_app.models import Shartnoma, Student, Kurs, Ustoz

class Tolov(models.Model):
    years = (
        ("2022", "2022"),
        ("2023", "2023"),
        ("2024", "2024"),
        ("2025", "2025"),
    )

    months = (
        ("January", "January"),
        ("February", "February"),
        ("March", "March"),
        ("April", "April"),
        ("May", "May"),
        ("June", "June"),
        ("Jule", "Jule"),
        ("August", "August"),
        ("September", "September"),
        ("October", "October"),
        ("November", "November"),
        ("December", "December"),
    )
    shartnoma = models.ForeignKey(Shartnoma, on_delete=models.SET_NULL, null=True)
    ustoz = models.ForeignKey(Ustoz, on_delete=models.SET_NULL, null=True)
    kurs = models.ForeignKey(Kurs, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    yil = models.CharField(max_length=10, choices=years)
    tolov_oyi = models.CharField(max_length=15, choices=months)
    chegirma_status = models.CharField(max_length=10, default="yo'q")
    ch_sababi = models.CharField(max_length=50)
    ch_miqdori = models.PositiveIntegerField()
    t_sanasi = models.DateField()
    kassir = models.CharField(max_length=30)
    tolashi_lozim = models.PositiveIntegerField()
    naqd = models.PositiveIntegerField()
    bank = models.PositiveIntegerField()
    plastik = models.PositiveIntegerField()
    click = models.PositiveIntegerField()
    jami_toladi = models.PositiveIntegerField()
    jami_qoldi = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.student.ism} {self.student.familya} ({self.jami_toladi})"