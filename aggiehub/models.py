from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=70, blank=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text
    
    def isToxic(self):
        return True if self.toxic.score > 0.5 else False


class Toxic(models.Model):
    post = models.OneToOneField(
        Post,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    score = models.FloatField(default=None)

    def __str__(self):
        return "'{}' has a toxicity score of '{}'".format(self.post, self.score)

    def isToxic(self):
        return True if self.score > 0.5 else False


class Claim(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resolved = models.BooleanField(default=False)


class Survey(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    SCORE_CHOICES = zip(range(1, 6), range(1, 6))
    score = models.IntegerField(choices=SCORE_CHOICES, blank=True)
    is_completed = models.BooleanField(default=False)
