from django.test import TestCase

from products.models import Category, Favorite, Product, Store
from users.models import User


class ProductTestsModels(TestCase):

    def test_models_category_product(self):
        category = Category.objects.create(name="pizza")
        self.assertEquals(category.name, "pizza")

    def test_models_store_product(self):
        store = Store.objects.create(name="auchan")
        self.assertEquals(store.name, "auchan")

    def test_models_product(self):
        category = Category.objects.create(name="pizza")
        product = Product.objects.create(
            id=1,
            id_category=category,
            product_name_fr="pizza jambon",
            nutrition_grade_fr="b"
        )
        self.assertEquals(product.id, 1)
        self.assertEquals(product.id_category, category)
        self.assertEquals(product.product_name_fr, "pizza jambon")
        self.assertEquals(product.nutrition_grade_fr, "b")

    def test_models_favorite_user(self):
        category = Category.objects.create(name="pizza")
        product = Product.objects.create(
            id=1,
            id_category=category,
            product_name_fr="pizza jambon",
            nutrition_grade_fr="b"
        )

        substitute = Product.objects.create(
            id=2,
            id_category=category,
            product_name_fr="pizza fromage",
            nutrition_grade_fr="a"
        )

        user = User.objects.create_user(
            username="UtilisateurTest",
            first_name="utilisateur",
            last_name="Test",
            password="Azertyu&4552"
        )

        Favorite.objects.create(
            user=user,
            substitute=substitute,
            product=product
        )
        favorite = Favorite.objects.all().first()
        self.assertEqual(favorite.user, user)
        self.assertEqual(favorite.substitute, substitute)
        self.assertEqual(favorite.product, product)
