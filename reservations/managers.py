from django.db import models


class CustomReservationManager(models.Manager):
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesnotExist:
            return None
