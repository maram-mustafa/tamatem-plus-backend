from django.db import models


class BaseModel(models.Model):
    """Inheriting this model will create timestamps fields.

    Since most of the models have timestamp fields so we created a
    base model that can be inherited to follow the DRY principle
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Model options."""

        abstract: bool = True

    def __str__(self) -> str:
        """Return a string representation of the object.

        Returns:
            str: A string representation of the object,
            which is the created_at attribute.
        """
        return self.created_at
