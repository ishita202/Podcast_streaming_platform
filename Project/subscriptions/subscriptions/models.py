from django.db import models
from django.conf import settings
from datetime import timedelta, date

class SubscriptionPlan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Each user has their own plans
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField()  # Number of days the plan lasts

    def __str__(self):
        return f"{self.name} - {self.user.username}"  # Show user ownership

class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        """ Ensure start_date is set before calculating end_date """
        if not self.start_date:
            self.start_date = date.today()
        if not self.end_date and self.plan.duration_days:
            self.end_date = self.start_date + timedelta(days=self.plan.duration_days)
        super().save(*args, **kwargs)
