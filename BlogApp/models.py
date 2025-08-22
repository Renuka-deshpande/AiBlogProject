from django.db import models

class SiteConfig(models.Model):
    site_name = models.CharField(max_length=100, unique=True)
    site_description = models.TextField(blank=True)
    site_logo = models.ImageField(upload_to='site_logos/', blank=True, null=True)
    site_favicon = models.ImageField(upload_to='site_favicons/', blank=True, null=True)

    def __str__(self):
        return self.site_name
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
    
