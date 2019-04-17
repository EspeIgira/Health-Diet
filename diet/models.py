from django.db import models

class Image(models.Model):
    name = models.CharField(max_length =30)
    image_name = models.ImageField(upload_to='diets/')
    description = models.TextField()
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


    @classmethod
    def search_by_category(cls,name):
        category = Category.objects.filter(name__icontains=name).all()
        images=None
        for i in category:
            print(i)
            images=cls.objects.filter(category=i.id)
        return images


    @classmethod
    def get_image(cls,id):
        return Image.objects.get(id=id)


class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    @classmethod
    def search_by_category(cls,name):
        category = cls.objects.filter(name__icontains=name).first()
        images=Image.objects.filter(category=category)
        return images


class Comment(models.Model):
    
    comments = models.CharField(max_length =30)
    image = models.ForeignKey(Image, null=True, blank=True)

    def __str__(self):
        return self.name

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()


   
   
