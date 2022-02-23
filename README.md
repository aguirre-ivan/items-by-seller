# Products by seller

Script realizado en Python que recorre los elementos de uno o más `seller_id` de un sitio determinado `site_id` y genera un archivo de LOG, el cual contiene los siguientes datos de cada ítem:
```
"id" del ítem, "title" del item, "category_id" donde está publicado, "name" de la categoria
```

## Funcionamiento

Cambiar a preferencia las siguientes variables:
- SELLER_ID: Representa una lista que contiene uno o más seller_id, de los cuales se quiere obtener sus productos
- SITE_ID: ID del sitio donde se quiere realizar la busqueda. POr jemplo = "MLA"

```
$ python products_by_seller.py
```

## Ejemplo de uso

A modo de ejemplo se encuentra [products.log](https://github.com/aguirre-ivan/products-by-seller/products.log), el cual es el resultado de recorrer los items publicados por el `seller_id = 179571326` del `site_id = "MLA"`

## Elaboración

Aguirre, Iván Gonzalo

Fecha: 2022-02