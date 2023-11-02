from typing import List
from models import FlowerBundle


pricing_info = {
    "R12": {
        5: 6.99,
        10: 12.99,
    },
    "L09": {
        3: 9.95,
        6: 16.95,
        9: 24.95,
    },
    "T58": {
        3: 5.95,
        5: 9.95,
        9: 16.99,
    },
}


def create_bundles(product_code: str) -> List[FlowerBundle]:

  if product_code == 'R12':
    return [
        FlowerBundle(quantity=5, price=6.99, name='Roses'),
        FlowerBundle(quantity=10, price=12.99, name='Roses')]

  if product_code == 'L09':
    return [
        FlowerBundle(quantity=3, price=9.95, name='Lilies'),
        FlowerBundle(quantity=6, price=16.95, name='Lilies'),
        FlowerBundle(quantity=9, price=24.95, name='Lilies')]

  if product_code == 'T58':
    return [
        FlowerBundle(quantity=3, price=5.95, name='Tulips'),
        FlowerBundle(quantity=5, price=9.95, name='Tulips'),
        FlowerBundle(quantity=9, price=16.95, name='Tulips')]

  raise Exception('Invalid product code')
