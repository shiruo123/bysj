from django.db import models

# Create your models here.


class UserAccount(models.Model):

    user = models.CharField(max_length=6)
    password = models.CharField(max_length=16)


class TiKu_xzt(models.Model):

    t = models.CharField(max_length=300)
    a = models.CharField(max_length=100)
    b = models.CharField(max_length=100)
    c = models.CharField(max_length=100)
    d = models.CharField(max_length=100)
    daan = models.CharField(max_length=4)


class TiKu_pdt(models.Model):

    t = models.CharField(max_length=300)
    a = models.CharField(max_length=4)
    b = models.CharField(max_length=4)
    daan = models.CharField(max_length=1)


class TiKu_xzt1(models.Model):

    t = models.CharField(max_length=300)
    a = models.CharField(max_length=100)
    b = models.CharField(max_length=100)
    c = models.CharField(max_length=100)
    daan = models.CharField(max_length=3)


class KaoShi(models.Model):

    a = models.CharField(max_length=50)
    img = models.CharField(max_length=50, null=True)
    other = models.CharField(max_length=50, null=True)


class ChengJi(models.Model):

    key_user_a = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    keu_KaoShi_b = models.ForeignKey(KaoShi, on_delete=models.CASCADE)
    fenshu = models.CharField(max_length=10, null=True)
