import re
from typing import Optional, List
import logging
from models import FlowerOrder

logger = logging.getLogger(__name__)


def parse_order(input_string: str) -> Optional[FlowerOrder]:
  pattern = r'(\d+)\s+([A-Z]+\d+)'
  match = re.match(pattern, input_string)

  if match:
    return FlowerOrder(quantity=int(match.group(1)), flower_code=match.group(2))

  return None


def parse_user_order() -> List[FlowerOrder]:
  try:
    product_lines = int(
        input("How many product lines you want to add in this order? "))
    orders = []

    for i in range(product_lines):
      order_string = input(f"Enter quantity & product code {i+1}: ")
      order = parse_order(order_string)
      if order:
        orders.append(order)
      else:
        logger.warn('Invalid product input. E.g. 10 R12')

    return orders
  except ValueError:
    logger.error('Invalid input')
