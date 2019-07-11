from django.db import models
class Board(models.Model):
    title = models.CharField(max_length=64, verbose_name="Product")
    content = models.TextField(null = True, blank=True, verbose_name="Description")
    price = models.FloatField(null=True, blank=True, verbose_name="Price")
    published = models.DateTimeField(auto_now_add=True, db_index=True,
                                     verbose_name="Published by")
    rubric = models.ForeignKey("Rubric", null=True,
                               on_delete=models.PROTECT, verbose_name="Rubric")

    class Meta:
        verbose_name_plural = "Ads"
        verbose_name = "Ad"
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True,
                            verbose_name="title")

    def __str__(self):
        return self.name