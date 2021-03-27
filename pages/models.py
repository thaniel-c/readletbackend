from django.db import models

# Create your models here.
class Page(models.Model):
    name = models.CharField(blank=True, null=True, max_length=25)    #Name of the readlet 
    creation_date = models.DateTimeField(auto_now_add=True)          #Get and store creation date forever
    lastedit_date = models.DateTimeField(auto_now=True)              #Get on creation and update whenever there is an edit
    content = models.TextField(default="# This is a blank page...")  #TextField for raw markdown content
    content_HTML = models.TextField(default="<h1>This is a blank page...</h1>")  #TextField for markdown content converted to HTML

    def __str__(self):
        return self.name #Return name as string representation
    
    def __repr__(self):
        return self.name #Return name for debugging as well
    
    class Meta:
        ordering = ['lastedit_date'] #Order by the last edit date by default
    
