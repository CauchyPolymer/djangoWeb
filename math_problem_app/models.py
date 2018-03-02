from django.contrib.auth.hashers import make_password, check_password
from django.db import models

# Create your models here.


class Rating(models.Model):
    ratingSrl = models.AutoField(primary_key=True)

    su1 = models.IntegerField(blank=True, null=True)
    su2 = models.IntegerField(blank=True, null=True)
    mi1 = models.IntegerField(blank=True, null=True)
    mi2 = models.IntegerField(blank=True, null=True)
    givec = models.IntegerField(blank=True, null=True)
    hwaktong = models.IntegerField(blank=True, null=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.ratingSrl)

    def store(self):
        self.save()
        return self

    def get_updated_at(self):
        return self.updatedAt.strftime("%Y. %m. %d")


class User(models.Model):
    userSrl = models.AutoField(primary_key=True)
    id = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    sex = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    school = models.CharField(max_length=200, blank=True, null=True)
    grade = models.CharField(max_length=20, blank=True, null=True)

    rate = models.ForeignKey(Rating, blank=True, null=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

    def store(self):
        self.save()
        return self

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password
        self.save()

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])
        return check_password(raw_password, self.password, setter)


