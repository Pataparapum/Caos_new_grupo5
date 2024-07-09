from django.db import models

# Create your models here.
class ReadUser(models.Model):
    id_ReadUser = models.AutoField(db_column="idReadUser", primary_key=True)
    userName = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=False, null=False, unique=True)
    password = models.CharField(max_length=999999, null=False)
    
    class Meta:
        db_table = "Read Users"
        verbose_name = "Read User"
        verbose_name_plural = "read Users"
    
    def __str__(self) -> str:
        text = self.userName + ' ' + self.email + ' (usuario lector)'
        return text
    
class WriteUser(models.Model):
    id_WriteUser = models.AutoField(db_column="idWriteUser", primary_key=True)
    userName = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=False, null=False, unique=True)
    empresa = models.CharField(max_length=50)
    password = models.CharField(max_length=999999, null=False)
    
    class Meta:
        db_table = "Write Users"
        verbose_name = "Write User"
        verbose_name_plural = "Write users"
        
    def __str__(self) -> str:
        text = self.userName + ' ' + self.email + ' (usuario escritor)'
        return text
        
class Newspaper(models.Model):
    id_Newspaper = models.AutoField(db_column="idNewspaper", primary_key=True)
    titulo = models.CharField(max_length=50)
    tipo_noticia = models.CharField(max_length=50)
    contenido = models.CharField(max_length=999999)
    user_fk = models.ForeignKey(WriteUser, db_column="idWriteUser", on_delete=models.CASCADE)
    
    class Meta:
        db_table = "Newspapers"
        verbose_name ="Newspaper"
        verbose_name_plural = "Newspapers"
        
    def __str__(self) -> str:
        text = self.titulo + ' noticia creada por: ' + self.user_fk.userName
        return text
    