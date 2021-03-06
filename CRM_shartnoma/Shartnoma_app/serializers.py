from rest_framework.serializers import ModelSerializer
from .models import Kurs, Ustoz, Student, Shartnoma

class KursSerializer(ModelSerializer):
    class Meta:
        model = Kurs
        fields = ["nom", "narx"]

class UstozSerializer(ModelSerializer):
    class Meta:
        model = Ustoz
        fields = ["ism", "yosh", "tel"]

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ["ism", "familya", "sharif", "jins", "tel1", "tel2", "status"]

class ShartnomaSerializer(ModelSerializer):
    class Meta:
        model = Shartnoma
        fields = ["K", "shartnoma_raqami", "student", "kurs", "ustoz", "kunlari", "kurs_vaqti", "guruh_nomi", "tuzuvchi", "sinov_dars_sanasi", "status"]
