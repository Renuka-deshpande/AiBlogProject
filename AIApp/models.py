from django.db import models

# Create your models here.
class AiQuery(models.Model):
    user = models.ForeignKey('UsersApp.CustomUser', on_delete=models.CASCADE)
    query_text = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query[:50]  # Return the first 50 characters of the query
    
