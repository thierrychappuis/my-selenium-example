from products.models import Category, Product, Store
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)


class DbAdd:
    """Add data class in the db"""

    def add_category(self, all_category):
        """Adding categories in the db"""

        for category in all_category:
            category = Category(name=category.name)
            category.save()

    def add_product(self, all_category):
        """Add all the data of a product in the db"""

        for category in all_category:
            current_category = Category.objects.get(name=category.name)

            for product in category.products:
                current_product = Product(
                    product_name_fr=product.product_name_fr[:499],
                    nutrition_grade_fr=product.nutrition_grade_fr,
                    id=product.id,
                    brands=product.brands,
                    id_category=current_category,
                    url=product.url,
                    image_url=product.image_url,
                    image_nutrition_url=product.image_nutrition_url
                )
                current_product.save()

                for store in product.stores.split(","):
                    current_store, created = Store.objects.get_or_create(
                        name=store)
                    current_store.save()
                    current_product.store.add(current_store)
    
