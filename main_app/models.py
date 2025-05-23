from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# A tuple of 2-tuples added above our models
MEALS = (("B", "Breakfast"), ("L", "Lunch"), ("D", "Dinner"))

CAT_IMAGES = [
    ("cat-in-box.svg", "Cat in Box"),
    ("cool-cat.svg", "Cool Cat"),
    ("happy-cat.svg", "Happy Cat"),
    ("nerd-cat.svg", "Nerd Cat"),
    ("sk8r-boi-cat.svg", "Skater Cat"),
    ("teacup-cat.svg", "Teacup Cat"),
    # Add any others you have in static/images
]
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("toy-detail", kwargs={"pk": self.id})


class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.CharField(
        max_length=100, choices=CAT_IMAGES, default="cat-in-box.svg")
        

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cat-detail", kwargs={"cat_id": self.id})


# Add new Feeding model below Cat model


class Feeding(models.Model):
    date = models.DateField("Feeding date")
    meal = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=MEALS,
        # set the default value for meal to be 'B'
        default=MEALS[0][0],
    )
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ["-date"]  # This line makes the newest feedings appear first
