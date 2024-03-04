from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date, datetime, timedelta


class AgeValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        user = value.get('author')
        birthdate = user.birthdate
        if birthdate is None:
            raise ValidationError('Author must have birthdate')
        else:
            age = (datetime.now().date() - birthdate) // timedelta(days=365)
            if age < 18:
                raise ValidationError('Author must be at least 18 years old')
            return value


class ForbiddenWordsValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        forbidden_words = ['чепуха', 'ерунда', 'глупость']
        header = value.get('header')
        for word in forbidden_words:
            if header in word or header == word:
                raise ValidationError('Forbidden words')


