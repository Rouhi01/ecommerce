from django.db import models


class ActiveQueryset(models.QuerySet):
    def activated(self):
        return self.filter(is_active=True)
