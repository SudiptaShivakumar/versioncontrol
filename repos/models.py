from django.db import models

class Repository(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class File(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Version(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    version_number = models.IntegerField()
    uploaded_file = models.FileField(upload_to='versions/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} v{self.version_number}"
