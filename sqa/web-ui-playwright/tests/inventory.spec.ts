import { test, expect } from '../fixtures';
import { isSorted } from '../utils/helpers';
import { products } from '../utils/testData';

test.describe('Inventory', () => {
  test(
    'sorting by price low to high should list prices in ascending order',
    {
      tag: '@regression',
      annotation: { type: 'testcase', description: 'TC-INV-001' },
    },
    async ({ loggedInInventory }) => {
      await loggedInInventory.sortBy('lohi');

      const prices = await loggedInInventory.productPrices();
      expect(prices.length).toBeGreaterThan(1);
      expect(isSorted(prices, 'asc', (a, b) => a - b)).toBe(true);
    },
  );

  test(
    'sorting by name Z to A should list names in descending order',
    {
      tag: '@regression',
      annotation: { type: 'testcase', description: 'TC-INV-002' },
    },
    async ({ loggedInInventory }) => {
      await loggedInInventory.sortBy('za');

      const names = await loggedInInventory.productNames();
      expect(names.length).toBeGreaterThan(1);
      expect(isSorted(names, 'desc', (a, b) => a.localeCompare(b))).toBe(true);
    },
  );

  test(
    'adding a product should update the cart badge and toggle the button',
    {
      tag: ['@smoke', '@regression'],
      annotation: { type: 'testcase', description: 'TC-CART-001' },
    },
    async ({ loggedInInventory }) => {
      await loggedInInventory.addToCart(products.backpack.slug);

      await expect(loggedInInventory.cartBadge).toHaveText('1');
      await expect(loggedInInventory.removeButton(products.backpack.slug)).toBeVisible();
    },
  );

  test(
    'removing a product should clear the cart badge',
    {
      tag: '@regression',
      annotation: { type: 'testcase', description: 'TC-CART-002' },
    },
    async ({ loggedInInventory }) => {
      await loggedInInventory.addToCart(products.backpack.slug);
      await loggedInInventory.removeFromCart(products.backpack.slug);

      await expect(loggedInInventory.cartBadge).toHaveCount(0);
      await expect(loggedInInventory.addToCartButton(products.backpack.slug)).toBeVisible();
    },
  );
});
