from products.openfoodfact.models.bdd.dbadd import DbAdd
from products.openfoodfact.models.categorydownloader import CategoryDownloader


def main():
    # Download the categories then the ranges
    category = CategoryDownloader()
    print('On télécharge les catégories et les produits !')
    all_categories = category.get_category()

    # Add the categories to the database
    add_db = DbAdd()
    print('On ajoute les catégories en base de données !')
    add_db.add_category(all_categories)
    print('On ajoute les produits de chaque catégorie en base de données !')
    add_db.add_product(all_categories)


if __name__ == "__main__":
    main()
