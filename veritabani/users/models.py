from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.timezone import timezone
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()


        img = Image.open(self.image.path)
        

        if img.height > 300 or img.width >300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class ForeignLanguageModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=100,verbose_name='Yabancı Dil')
    language_level = models.CharField(max_length=100,verbose_name='Yabancı Dil Seviyesi')


    def __str__(self):
        return f'{self.user.username} ForeignLanguageModel'

class ContactInformationModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tel_number = models.CharField(max_length=11, verbose_name='Telefon numarası')
    adresses = models.CharField(max_length=50,verbose_name='Adres')

    def __str__(self):
        return f'{self.user.username} ContactInformationModel'


class CertificatedModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name='Sertifika İsmi')
    date = models.DateField(verbose_name='Alınan Tarih')
    getWhere = models.CharField(max_length=50, verbose_name='Alınan Yer')

    def __str__(self):
        return f'{self.user.username} CertificatedModel'


class IdInformationModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    tc_no = models.CharField(max_length=11,verbose_name='Tc Kimlik Numarası')
    birth_place = models.CharField(max_length=20,verbose_name='Doğum Yeri')
    birth_day = models.DateTimeField(verbose_name='Doğum Tarihi',auto_now_add=False)
    city_of_live = models.CharField(max_length=20,verbose_name='Yaşanılan yer')

    def __str__(self):
        return f'{self.user.username} IdInformationModel'

class EducationInformationModel(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    graduated_from_highscool = models.CharField(max_length=100,verbose_name='Mezun Olunan lise')
    graduated_from_univesity = models.CharField(max_length=100,verbose_name='Mezun Olunan Üniversite')


    def __str__(self):
        return f'{self.user.username} EducationInformation'

class CvModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    flanguage = models.OneToOneField(ForeignLanguageModel, on_delete=models.CASCADE)
    einformation = models.OneToOneField(EducationInformationModel, on_delete=models.CASCADE)
    idinf = models.OneToOneField(IdInformationModel, on_delete=models.CASCADE)
    ceftificatedinf = models.OneToOneField(CertificatedModel, on_delete=models.CASCADE)
    continf = models.OneToOneField(ContactInformationModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} CvModel'

class CompanyModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employeeCompany = models.CharField(max_length=50, verbose_name='Çalıştığı firma')

    def __str__(self):
        return f'{self.user.username} Company' 



class JobNewsModel(models.Model):
    JobTag = models.CharField(max_length=50, verbose_name='İş Başlığı')
    employerCompany = models.CharField(max_length=50, verbose_name='İşveren Firma')
    jobDescription = models.TextField(verbose_name='İş Tanımı ve Aranan özellikler')
    pozitionInformation = models.TextField(verbose_name='Pozisyon Bilgileri')

    def __str__(self):
        return self.JobTag







