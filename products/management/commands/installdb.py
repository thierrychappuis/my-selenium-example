from django.core.management.base import BaseCommand, CommandError

from products.openfoodfact.models.bdd.dbadd import DbAdd
from products.openfoodfact.models.categorydownloader import CategoryDownloader


class Command(BaseCommand):
    help = 'Get product OpenFood'


    def handle(self, *args, **options):
        # Download the categories then the ranges
        category = CategoryDownloader()
        self.stdout.write('On télécharge les catégories et les produits !')
        all_categories = category.get_category()

        # Add the categories to the database
        add_db = DbAdd()
        self.stdout.write('On ajoute les catégories en base de données !')
        add_db.add_category(all_categories)
        self.stdout.write('On ajoute les produits de chaque catégorie en base de données !')
        add_db.add_product(all_categories)
