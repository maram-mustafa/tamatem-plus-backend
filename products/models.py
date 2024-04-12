from django.core.validators import FileExtensionValidator
from django.db import models

from core.models import BaseModel

# Create your models here.


def resume_upload_path(instance, file_name: str) -> str:
    """Create a unique path for media based on the instance and file_name.

    This function will create a unique timestamp using the created time
    to create a unique path

    Args:
        instance (Product): Instance from Product that have been created.
        file_name (str): The name of the file that have been uploaded.

    Returns:
        str: a unique path for uploading the file.
    """
    # Get the name of the product and sanitize it (e.g., remove spaces)
    name: str = instance.name.replace(" ", "_")
    # We will use the created date so the products with same name
    # W cannot use the id because it is None at this point
    created_date_str: str = instance.created_at.strftime("%Y_%m_%d_%H_%M_%S_%f")[:-3]
    # Build the dynamic upload path using the products's full_name
    return "products/{0}-{1}/{2}".format(name, created_date_str, file_name)


class Product(BaseModel):
    name = models.CharField(
        max_length=255, verbose_name="Name", blank=False, null=False
    )
    description = models.TextField(verbose_name="Description", blank=False, null=False)
    price = models.FloatField(verbose_name="Price", blank=False, null=False)
    image = models.FileField(
        upload_to=resume_upload_path,
        verbose_name="Image",
        validators=[FileExtensionValidator(allowed_extensions=["png", "jpg", "jpeg"])],
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self) -> str:
        return self.name
