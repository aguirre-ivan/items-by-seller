# Items by seller

Script made in Python that iterates through one or more `seller_id` items from a `site_id` and generates a LOG file which contains the following info:

```
ítem "id", item "title", "category_id", category "name"
```
## Usage
1. Config variables:
   - SELLER_ID: List with one or more seller_id
   - SITE_ID: site ID where we want to search (for example "MLA")

2. Run [items_by_seller.py](https://github.com/aguirre-ivan/products-by-seller/blob/main/items_by_seller.py)
```
$ python items_by_seller.py
```
## Example

[items.log](https://github.com/aguirre-ivan/products-by-seller/blob/main/items.log), which is the result of `seller_id = 179571326` and `site_id = "MLA"`
