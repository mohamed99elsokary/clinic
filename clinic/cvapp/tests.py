from rest_framework import status
from rest_framework.test import APITestCase
from . import models


def setup():
    models.cv.objects.create(name="isudf")
    models.Field.objects.create(field="isudf", index=1)
    models.ScientificDegree.objects.create(scientific_degree="isudf", index=1)
    models.Experience.objects.create(experience="isudf", index=1)
    models.Skill.objects.create(skill="isudf", index=1)
    models.Other.objects.create(name="isudf", text="uashdiauhd", index=1)


class CVTestCase(APITestCase):
    def test_get_empty_cv(self):
        response = self.client.get("/api/cv")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_valid_cv(self):
        setup()
        response = self.client.get("/api/cv")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
