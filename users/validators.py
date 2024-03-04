from django.core.exceptions import ValidationError


def validate_password(password):
    if len(password) < 8:
        raise ValidationError('Password must be at least 8 characters long.', code='password_too_short')
    if not any(char.isdigit() for char in password):
        raise ValidationError('Password must contain at least one number.', code='password_no_number')
