from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    price = models.FloatField()
    amount = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def tag_list(self):
        # l = []
        # for tag in self.tags.all():
        #     l.append(tag.name)
        # return l
        return [tag.name for tag in self.tags.all()]

    @property
    def filtered_reviews(self):
        return self.product_reviews.filter(stars__gt=3)


CHOICES = (
    (1, '*'),
    (2, 2 * '* '),
    (3, 3 * '* '),
    (4, 4 * '* '),
    (5, 5 * '* '),
)


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='product_reviews')
    stars = models.IntegerField(choices=CHOICES, default=1)

    def __str__(self):
        return self.text
