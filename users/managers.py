from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self , email, username, Phone, Address, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not username:
            raise ValueError("Users must Username")

        user = self.model(
            email=self.normalize_email(email), username=username, Address = Address, Phone=Phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, Phone, Address, password):
        """Create and save a new superuser with given details"""

        user = self.create_user(email, username,Phone, Address, password)

        user.admin = True
        user.staff = True

        user.save(using=self._db)
        return user