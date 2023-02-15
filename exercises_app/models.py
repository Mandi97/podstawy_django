from django.db import models


GENRES = (
    (-1, 'not definied'),
    (0, 'rock'),
    (1, 'metal'),
    (2, 'pop'),
    (3, 'hip-hop'),
    (4, 'electronic'),
    (5, 'reggae'),
    (6, 'other'),
)


class Band(models.Model):
    name = models.CharField(max_length=64)
    year = models.IntegerField(null=True)
    still_active = models.BooleanField(default=True)
    genre = models.IntegerField(choices=GENRES, default=-1)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


STATUS = (
    (1, 'W trakcie pisania'),
    (2, 'Czeka na akceptację redaktora'),
    (3, 'Opublikowany'),
)


class Article(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=54, null=True, blank=True)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    published = models.DateTimeField(null=True, blank=True)
    unpublished = models.DateField(null=True, blank=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


RATING = (
    (0, 'brak gwiazdek'),
    (1, '*'),
    (2, '**'),
    (3., '***'),
    (4., '****'),
    (5., '*****'),
)


class Album(models.Model):
    title = models.TextField()
    year = models.IntegerField()
    rating = models.IntegerField(choices=RATING)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=128)
    duration = models.TimeField(null=True, blank=True)
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='songs',
    )

    def __str__(self):
        return self.title
