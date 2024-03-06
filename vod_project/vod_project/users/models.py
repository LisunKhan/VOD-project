from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for vod_test.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    phone = CharField(_("Phone Number"), blank=True, max_length=100)
    birth_date = DateField(null=True, blank=True)
    gender = CharField(_("Gender"), choices=GENDER_CHOICES, max_length=1, blank=True)
    address = CharField(_('User Address'), blank=True, max_length=300, null=True)

    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
