from datetime import datetime

from django.db import models

# Create your models here.


class Exercise(models.Model):
    name = models.CharField(50)
    description = models.TextField(null=True, blank=True)

    @property
    def format_description(self) -> str:
        return self.description.replace('\n', '<br>')

    def __str__(self):
        return self.name


class Day(models.Model):
    exercise_id = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    day_of_the_week = models.IntegerField()

    def __str__(self):
        return f'({self.day_of_the_week})'


class Done(models.Model):
    exercise_id = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    day_id = models.ForeignKey(Day, on_delete=models.CASCADE)
    sets = models.IntegerField(null=True, blank=True)
    reps = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'({self.exercise_id})'



# DAY_OF_THE_WEEK = {
#     1: _(u'Monday'),
#     2: _(u'Tuesday'),
#     3: _(u'Wednesday'),
#     4: _(u'Thursday'),
#     5: _(u'Friday'),
#     6: _(u'Saturday'),
#     7: _(u'Sunday'),
# }
#
#
# class DayOfTheWeekField(models.IntegerField):
#     """
#     Django Model field for representing Day of week
#     """
#     def __init__(self, *args, **kwargs):
#         kwargs['choices'] = tuple(sorted(DAY_OF_THE_WEEK.items()))
#         super(DayOfTheWeekField, self).__init__(*args, **kwargs)

# LOAN_STATUS = (
#         ('m', 'Maintenance'),
#         ('o', 'On loan'),
#         ('a', 'Available'),
#         ('r', 'Reserved'),
#     )
#
#     status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')




# class Post(models.Model):
#     title = models.CharField(50)
#     text = models.TextField()
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     date_create = models.DateTimeField(default=timezone.now)
#
#
#     @property
#     def href(self) -> str:
#         return f'http://127.0.0.1:8000/article/{self.id}'
#
#     @property
#     def cut_text(self) -> str:
#         MAX_COUNT_SYMBOLS: int = 80
#
#         if len(self.text) <= MAX_COUNT_SYMBOLS:
#             return self.text
#
#         return f'{self.text[:MAX_COUNT_SYMBOLS]}...'
#
#
#     @property
#     def decorate_date(self) -> str:
#         date_create: datetime = self.date_create
#
#         return date_create.strftime('%d.%m.%Y %H:%M')
#
#     @property
#     def safe_text(self) -> str:
#         return self.text.replace('\n', '<br>')
#
#     class Meta:
#         ordering: List[str] = ['-date_create']
#
#     def __str__(self):
#         return self.title
#
#
# class Comment(models.Model):
#     text = models.TextField()
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
#     date_create = models.DateTimeField(default=timezone.now)
#
#     @property
#     def decorate_date(self) -> str:
#         date_create: datetime = self.date_create
#
#         return date_create.strftime('%d.%m.%Y %H:%M')
#
#     class Meta:
#         ordering: List[str] = ['-date_create']
#
#     def __str__(self):
#         return self.text
#
#
# class Mark(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
#
#     is_negative = models.BooleanField(default=False)
#     date_create = models.DateTimeField(default=timezone.now)
#
#     def __str__(self) -> str:
#         return f'({self.user_id})' \
#                f'({self.post_id})' \
#                f'[{"-" if self.is_negative else "+"}]'
