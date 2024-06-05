from diary_app.models import Exercise, Day


class ExerciseController:
    def __init__(self) -> None:
        self.__exercises1 = None
        self.__exercises2 = None
        self.__exercises3 = None
        self.__exercises4 = None
        self.__exercises5 = None
        self.__exercises6 = None
        self.__exercises7 = None

    @property
    def _1_exercises(self):
        if not self.__exercises1:
            self.__exercises1 = Day.objects.filter(day_of_the_week=1)

        return self.__exercises1

    def get_1_exercises(self):
        return self._1_exercises

    @property
    def _2_exercises(self):
        if not self.__exercises2:
            self.__exercises2 = Day.objects.filter(day_of_the_week=2)

        return self.__exercises2

    def get_2_exercises(self):
        return self._2_exercises

    @property
    def _3_exercises(self):
        if not self.__exercises3:
            self.__exercises3 = Day.objects.filter(day_of_the_week=3)

        return self.__exercises3

    def get_3_exercises(self):
        return self._3_exercises

    @property
    def _4_exercises(self):
        if not self.__exercises4:
            self.__exercises4 = Day.objects.filter(day_of_the_week=4)

        return self.__exercises4

    def get_4_exercises(self):
        return self._4_exercises

    @property
    def _5_exercises(self):
        if not self.__exercises5:
            self.__exercises5 = Day.objects.filter(day_of_the_week=5)

        return self.__exercises5

    def get_5_exercises(self):
        return self._5_exercises

    @property
    def _6_exercises(self):
        if not self.__exercises6:
            self.__exercises6 = Day.objects.filter(day_of_the_week=6)

        return self.__exercises6

    def get_6_exercises(self):
        return self._6_exercises

    @property
    def _7_exercises(self):
        if not self.__exercises7:
            self.__exercises7 = Day.objects.filter(day_of_the_week=7)

        return self.__exercises7

    def get_7_exercises(self):
        return self._7_exercises
