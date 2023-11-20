from django.test import TestCase

from AppBlogs.models import Articles


class ArticlesTests(TestCase):
   
    def test_create_article(self):
      
        article = Articles(title="title", subTitle="subTitle")
        article.save()

        # Compruebando el guardado en la DB

     
        self.assertEqual(Articles.objects.count(), 1)
        self.assertEqual(article.title, "title")
        self.assertEqual(article.subTitle, "subTitle")

    def test_articles_str(self):
        article = Articles(title="Viva", subTitle="Boca")
        article.save()

        # Compruebando el str
        self.assertEqual(article.__str__(), "Viva, Boca")

   

      