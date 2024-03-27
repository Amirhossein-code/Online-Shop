from django.db import models
from .customer import Customer


class Address(models.Model):
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    full_address = models.CharField(max_length=550)
    main = models.BooleanField(default=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="address"
    )

    def save(self, *args, **kwargs):
        """
        if the main is set to true we check to see if there is another instace saved as main
        if there is we set that to fasle and set the new one to True
        ensuring we have only 1 instance of address set to main for customer
        """
        if self.main:
            Address.objects.filter(customer=self.customer, main=True).exclude(
                pk=self.pk
            ).update(main=False)
        # If it is users first time creating an address and he sets main to false
        # this ensures it is main
        # if we have an address in databse it should have main = True for each customer
        if not self.pk:
            if (
                not Address.objects.filter(customer=self.customer)
                .exclude(pk=self.pk)
                .exists()
            ):
                self.main = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.city
