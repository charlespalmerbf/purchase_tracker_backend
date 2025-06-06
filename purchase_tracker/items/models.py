from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='items/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()

    def cost_per_day(self):
        from datetime import date
        days_since = (date.today() - self.purchase_date).days
        return float(self.price) / max(days_since, 1)
