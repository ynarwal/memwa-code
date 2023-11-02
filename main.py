from typing import List
import logging
import input_parser as parser
from models import FlowerBundle, FlowerOrder
import bundle_factory
import min_bundle_creator

logger = logging.getLogger(__name__)


def _group_by_quantity(bundles: List[FlowerBundle]):
  grouped_bundles = {}
  for bundle in bundles:
    quantity = bundle.quantity
    if quantity not in grouped_bundles:
      grouped_bundles[quantity] = []
    grouped_bundles[quantity].append(bundle)
  return grouped_bundles


def _price_format(price: float) -> str:
  return "{:.2f}".format(price)


def _print_order_bundle(order: FlowerOrder, bundles: List[FlowerBundle]):
  total = sum([bundle.price for bundle in bundles])

  groups = _group_by_quantity(bundles)

  print(f'{order.quantity} {order.flower_code} $ {_price_format(total)}')

  for quantity, bundles in groups.items():
    print(
        f'\t {len(bundles)} * {quantity} $ {_price_format(bundles[0].price)}')


def process_orders(orders: List[FlowerOrder]):
  for order in orders:
    flower_bundles = bundle_factory.create_bundles(order.flower_code)
    min_bundles = min_bundle_creator.create_min_bundle_combinations(
        order.quantity, flower_bundles)
    _print_order_bundle(order, min_bundles)


if __name__ == '__main__':
  orders = parser.parse_user_order()
  process_orders(orders)
