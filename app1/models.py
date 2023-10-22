from django.db import models

# Create your models here.


class UserAccount(models.Model):

    user = models.CharField(max_length=6)
    password = models.CharField(max_length=16)


class TiKu_xzt(models.Model):

    t = models.CharField(max_length=300)
    a = models.CharField(max_length=100)
    b = models.CharField(max_length=100)
    c = models.CharField(max_length=100, null=True)
    d = models.CharField(max_length=100, null=True)
    daan = models.CharField(max_length=4, null=True)


class KaoShi(models.Model):

    a = models.CharField(max_length=50)
    img = models.CharField(max_length=50, null=True)
    other = models.CharField(max_length=50, null=True)


class ChengJi(models.Model):

    key_user_a = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    keu_KaoShi_b = models.ForeignKey(KaoShi, on_delete=models.CASCADE)
    fenshu = models.CharField(max_length=10, null=True)


class TiKuGuanLi(models.Model):

    key_TiKu_a = models.ForeignKey(TiKu_xzt, on_delete=models.CASCADE)
    key_KaoShi_b = models.ForeignKey(KaoShi, on_delete=models.CASCADE)


class LunTan(models.Model):

    title = models.CharField(max_length=50, null=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    key_UserAccount = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

