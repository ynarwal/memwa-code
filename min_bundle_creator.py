from typing import Dict, List

from models import FlowerBundle


def _find_combination_sum(amount: int, bundles: List[FlowerBundle], memo: Dict):
  if amount in memo:
    return memo[amount]

  if amount < 0:
    return None

  if amount == 0:
    return []

  shortest_combination = None  # Initialize with None

  for bundle in bundles:
    result = _find_combination_sum(amount - bundle.quantity, bundles, memo)
    if result is not None:
      if shortest_combination is None or len(result) + 1 < len(shortest_combination):
        shortest_combination = [bundle] + result
        memo[amount] = shortest_combination

  return shortest_combination


"""
We are using memoisation to avoid duplicate calcualations.
This will be only noticable for large inputs
"""


def create_min_bundle_combinations(amount: int, bundles: List[FlowerBundle]) -> List[FlowerBundle]:
  ans = _find_combination_sum(amount, bundles, {})
  if ans is None:
    raise Exception(
        f'No bundle combination possible to create the order quantity {amount} from bundles {bundles}')
  return ans
