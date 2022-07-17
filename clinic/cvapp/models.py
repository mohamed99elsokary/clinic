from django.db import models

# Create your models here.


class cv(models.Model):
    name = models.CharField(max_length=300)


class Field(models.Model):
    cv = models.ForeignKey(
        cv, on_delete=models.CASCADE, default=1, related_name="fields"
    )
    field = models.CharField(max_length=300)
    index = models.IntegerField()

    class Meta:
        ordering = ("index",)

    def __str__(self):
        return self.field


class ScientificDegree(models.Model):
    cv = models.ForeignKey(
        cv, on_delete=models.CASCADE, default=1, related_name="scientific_degrees"
    )
    scientific_degree = models.CharField(max_length=300)
    index = models.IntegerField()

    class Meta:
        ordering = ("index",)

    def __str__(self):
        return self.scientific_degree


class Experience(models.Model):
    cv = models.ForeignKey(
        cv, on_delete=models.CASCADE, default=1, related_name="experiences"
    )
    experience = models.CharField(max_length=300)
    index = models.IntegerField()

    class Meta:
        ordering = ("index",)

    def __str__(self):
        return self.experience


class Skill(models.Model):
    cv = models.ForeignKey(
        cv, on_delete=models.CASCADE, default=1, related_name="skills"
    )
    skill = models.CharField(max_length=300)
    index = models.IntegerField()

    class Meta:
        ordering = ("index",)

    def __str__(self):
        return self.skill


class Other(models.Model):
    cv = models.ForeignKey(
        cv, on_delete=models.CASCADE, default=1, related_name="others"
    )
    name = models.CharField(max_length=300)
    text = models.CharField(max_length=300)
    index = models.IntegerField()

    class Meta:
        ordering = ("index",)

    def __str__(self):
        return self.name
