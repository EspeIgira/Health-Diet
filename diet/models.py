from django.db import models

class Image(models.Model):
    name = models.CharField(max_length =30)
    image_name = models.ImageField(upload_to='health/')
    description = models.TextField()
    comments = models.CharField(max_length =100)
    # category = models.ForeignKey(Category, null=True, blank=True)

    def __str__(self):
        return self.name


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update()
    
    def display_image(self):
        self.display()

    class Meta:
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name




class Comment(models.Model):
    
    comments = models.CharField(max_length =30)
    image = models.ForeignKey(Image, null=True, blank=True)

    def __str__(self):
        return self.name

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()


   
