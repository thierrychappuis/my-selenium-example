from django.test import TestCase


from products.models import Category, Product, Favorite
from users.models import User

class ProductTestsModels(TestCase):

    def test_models_favorite_user(self):
        # créer une catégorie
        category = Category.objects.create(name="pizza")
        # créer un produit
        product = Product.objects.create(
            id=1,
            id_category= category,
            product_name_fr="pizza jambon",
            nutrition_grade_fr="b")

        substitute = Product.objects.create(
            id=2,
            id_category= category,
            product_name_fr="pizza fromage",
            nutrition_grade_fr="a"
        )
        # créer un utilisateur
        user_create = User.objects.create_user(username="UtilisateurTest", first_name="utilisateur", last_name="Test", password="Azertyu&4552")
        # créer un favoris
        favorite = Favorite.objects.create(user=user_create, substitute=substitute, product=product)
        # authentifier ton utilisateur
        user = user_create.objects.get(username="UtilisateurTest")
        # self.client.get(vers url des favoris)
        self.client.get("favorites")
        # assertContains(response, 'pizza jambon')
        self.assertContains(response=substitute)
