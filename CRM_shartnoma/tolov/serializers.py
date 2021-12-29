from rest_framework.serializers import ModelSerializer
from .models import Tolov

class TolovSerializer(ModelSerializer):
    class Meta:
        model = Tolov
        fields = ["shartnoma", "ustoz", "kurs", "student", "yil", "tolov_oyi", "chegirma_status", "ch_sababi", "ch_miqdori",
                  "t_sanasi", "kassir", "tolashi_lozim", "naqd", "bank", "plastik", "click", "jami_toladi", "jami_qoldi"]
