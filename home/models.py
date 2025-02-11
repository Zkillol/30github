from django.db import models

class Post(models.Model):
    user = models.CharField('Владелец', max_length=50)
    square = models.IntegerField('Сколько кв метров')
    city = models.CharField('Город', max_length=50)
    street = models.CharField('Улица', max_length=50)
    year = models.IntegerField('Год постройки')  # ✅ Changed from DateField to IntegerField
    img = models.ImageField(upload_to='img/', null=True, blank=True)

    # Property type choices
    APARTMENT = 'apartment'
    HOUSE = 'house'

    PROPERTY_TYPE_CHOICES = [
        (APARTMENT, 'Квартира'),
        (HOUSE, 'Дом'),
    ]

    title = models.CharField(max_length=255)
    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPE_CHOICES,
        default=APARTMENT
    )

    def __str__(self):
        return f"{self.title} - {self.get_property_type_display()}"
