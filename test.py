import unittest
from typing import List
from models import FlowerBundle
import min_bundle_creator


def _sort_bundle_list(bundles: List[FlowerBundle]):
  return sorted(bundles, key=lambda bundle: bundle.quantity)


class TestMinBundleCreator(unittest.TestCase):

  def test_min_bundle_creator(self):
    # Arrange

    test_data = {
        'R12': (
            10,
            [
                FlowerBundle(quantity=5, price=6.99, name='Roses'),
                FlowerBundle(quantity=10, price=12.99, name='Roses')
            ], [
                FlowerBundle(quantity=10, price=12.99, name='Roses')
            ]),

        'L09': (
            15,
            [
                FlowerBundle(quantity=3, price=9.95, name='Lilies'),
                FlowerBundle(quantity=6, price=16.95, name='Lilies'),
                FlowerBundle(quantity=9, price=24.95, name='Lilies')
            ], [
                FlowerBundle(quantity=6, price=16.95, name='Lilies'),
                FlowerBundle(quantity=9, price=24.95, name='Lilies')
            ]),

        'L09': (
            13,
            [
                FlowerBundle(quantity=3, price=5.95, name='Tulips'),
                FlowerBundle(quantity=5, price=9.95, name='Tulips'),
                FlowerBundle(quantity=9, price=16.95, name='Tulips')
            ], [
                FlowerBundle(quantity=5, price=9.95, name='Tulips'),
                FlowerBundle(quantity=5, price=9.95, name='Tulips'),
                FlowerBundle(quantity=3, price=5.95, name='Tulips')
            ])
    }

    for k, values in test_data.items():
      # Act
      res = min_bundle_creator.create_min_bundle_combinations(
          values[0], values[1])

      # Assert
      self.assertEquals(_sort_bundle_list(res), _sort_bundle_list(res))


if __name__ == "__main__":
  unittest.main()
