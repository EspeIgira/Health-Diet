from django.test import TestCase
from .models import Image,Category,Comment

class ImageTestClass(TestCase):


    def setUp(self):
        # Creating a new editor and saving it
        self.name= Image(name = 'image', image_name ='diet',description = 'description')
        self.name.save_image()

        # Creating a new tag and saving it
        self.new_comment = comments(name = 'testing')
        self.new_comment.save()

        self.new_category= Category(name = 'Test Category',post = 'This is a random test Post',image = self.name)
        self.new_category.save()

        self.new_category.comments.add(self.new_comment)

    def tearDown(self):
        Image.objects.all().delete()
        comments.objects.all().delete()
        Category.objects.all().delete()

    def health_of_day(self):
        images = Image.images()
        self.assertTrue(len(images)>0)

    def test_delete_method(self):
       self.food.save_image()
       images = Image.objects.all()
       self.assertTrue(len(images) > 0)

    def test_display_method(self):
        self.food.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_update_method(self):
        self.food.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
       

    
