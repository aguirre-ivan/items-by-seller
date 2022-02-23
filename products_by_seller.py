import requests
import logging

# USO
# Cambiar el seller_id y/o site_id por lo requerido

SITE_ID = 'MLA'
SELLER_ID = '179571326'
URL_PRODUCTS = f"https://api.mercadolibre.com/sites/{SITE_ID}/search?seller_id={SELLER_ID}"


def get_category_name(category_id):
	"""
	Devuelve el nombre de la categoria asociada a category_id
	"""
	url_category_info = f"https://api.mercadolibre.com/categories/{category_id}"
	category_name_request = requests.get(url_category_info)

	return category_name_request.json()['name']


def log_seller_products(seller_id):
	"""
	Agrega al archivo de LOG los datos de los productos asociados al seller_id en el siguiente formato:
	"id" del ítem, "title" del item, "category_id" donde está publicado, "name" de la categoría.
	"""
	products_requests = requests.get(URL_PRODUCTS)
	products_requests_dict = products_requests.json()

	logging.basicConfig(filename='products.log', level="INFO")

	for product in products_requests_dict['results']:

		product_id = product['id']
		category_id = product['category_id']
		category_name = get_category_name(category_id)

		line = f"{product_id},{category_id},{category_name}"
		logging.info(line)


def main():
	log_seller_products(SELLER_ID)

if __name__ == '__main__':
	main()
