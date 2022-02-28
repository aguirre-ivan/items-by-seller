# DESCRIPCION:
# Genera un archivo LOG con los ítems publicados por SELLER_ID del site SITE_ID
# Se generan lineas por cada producto con el siguiente formato:
# "id" del ítem, "title" del item, "category_id" donde está publicado, "name" de la categoría.

# ELABORACION: Aguirre, Iván Gonzalo (2022-02)

# FUNCIONAMIENTO:
# Simplemente cambiar el SELLER_ID y/o SITE_ID por lo requerido
# $ python products_by_seller.py


import requests
import logging


SITE_ID = 'MLA'
SELLER_ID = ['179571326']


def get_category_name(category_id):
	"""
	Devuelve el nombre de la categoria asociada a category_id
	"""
	url_category_info = f"https://api.mercadolibre.com/categories/{category_id}"
	category_name_request = requests.get(url_category_info)

	return category_name_request.json()['name']


def log_seller_products(url_seller_products):
	"""
	Agrega al archivo de LOG los datos de los productos asociados al seller_id en el siguiente formato:
	"id" del ítem, "title" del item, "category_id" donde está publicado, "name" de la categoría.
	"""
	products_requests = requests.get(url_seller_products)
	products_requests_dict = products_requests.json()

	logging.basicConfig(filename='products.log', level="INFO")

	for product in products_requests_dict['results']:

		product_id = product['id']
		item_title = product['title']
		category_id = product['category_id']
		category_name = get_category_name(category_id)

		line = f"{product_id}, {item_title}, {category_id}, {category_name}"
		logging.info(line)


def main():
	for seller in SELLER_ID:
		url_seller_products = f"https://api.mercadolibre.com/sites/{SITE_ID}/search?seller_id={seller}"
		log_seller_products(url_seller_products)


if __name__ == '__main__':
	main()