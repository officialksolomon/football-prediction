from django.db.models.base import Model
from django.forms import ModelForm
from .models import Prediction


class PredictionForm(ModelForm):
    class Meta:
        model = Prediction
        fields = ['player', 'match', 'prediction']
