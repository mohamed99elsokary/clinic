from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    cover = models.ImageField(
        upload_to="media/service",
        height_field=None,
        width_field=None,
        max_length=None,
        null=True,
        blank=True,
    )
    index = models.IntegerField()
    duration = models.IntegerField()
    is_online = models.BooleanField(default=False)

    class Meta:
        ordering = ("index",)

    def __str__(self):
        return self.name


class ServiceDetails(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="service_details",
    )
    image = models.ImageField(
        upload_to="media/service_details",
        height_field=None,
        width_field=None,
        max_length=None,
        null=True,
        blank=True,
    )
    text = models.TextField()
    index = models.IntegerField()

    class Meta:
        ordering = ("index",)

    def __str__(self):
        return self.service.name
