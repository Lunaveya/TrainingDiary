from django.forms import Form, CharField, Textarea, IntegerField


class SetsRepsWeightForm(Form):
    sets = IntegerField(label='Подходы')
    reps = IntegerField(label='Повторения')
    weight = IntegerField(label='Вес')
