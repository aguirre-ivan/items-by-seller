# DESCRIPTION:
# Generates a LOG file (items.log) with the items published in site SITE_ID filtered by SELLER_ID
# Format lines:
# ítem "id", item "title", "category_id", category "name"

# WRITTEN BY: 
# Aguirre, Iván Gonzalo (2022-02)

# USAGE:
# Just config SELLER_ID and/or SITE_ID
# Run items_by_seller.py
# $ python items_by_seller.py


import requests
import logging


SITE_ID = 'MLA'
SELLER_ID = ['179571326']


def get_category_name(category_id):
	"""
	Returns category name associated to category_id

	Args:
		category_id (int)

	Returns:
		str: category name
	"""
	url_category_info = f"https://api.mercadolibre.com/categories/{category_id}"
	category_name_request = requests.get(url_category_info)

	return category_name_request.json()['name']


def log_seller_items(url_seller_items):
	"""
	Adds seller items info to log file in format:
	ítem "id", item "title", "category_id", category "name"

	Args:
		url_seller_items (str): url of items by seller_id
	"""
	items_requests = requests.get(url_seller_items)
	items_requests_dict = items_requests.json()

	logging.basicConfig(filename='items.log', level="INFO", format='%(message)s')

	for item in items_requests_dict['results']:

		item_id = item['id']
		item_title = item['title']
		category_id = item['category_id']
		category_name = get_category_name(category_id)

		line = f"{item_id}, {item_title}, {category_id}, {category_name}"
		logging.info(line)


def generate_log_file():
	for seller in SELLER_ID:
		url_seller_items = f"https://api.mercadolibre.com/sites/{SITE_ID}/search?seller_id={seller}"
		log_seller_items(url_seller_items)


if __name__ == '__main__':
	generate_log_file()
