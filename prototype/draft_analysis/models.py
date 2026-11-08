from django.db import models


class DMHCDecision(models.Model):
    reference_id = models.CharField(max_length=100, unique=True)
    report_year = models.IntegerField()
    treatment_category = models.CharField(max_length=255)
    review_type = models.CharField(max_length=255)
    determination = models.CharField(max_length=255)

    def __str__(self):
        return self.reference_id