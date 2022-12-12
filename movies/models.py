from django.db import models


class RatingTypes(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


# N - 1 (usuário)
class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, blank=True, null=True)
    rating = models.CharField(
        max_length=10,
        choices=RatingTypes.choices,
        default=RatingTypes.G,
    )
    synopsis = models.TextField(blank=True, null=True)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies",
        null=True,
    )

    def __repr__(self) -> str:
        return f"<Movie [{self.id}] - {self.title}"
