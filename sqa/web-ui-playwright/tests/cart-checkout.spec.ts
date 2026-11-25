import { test, expect } from '../fixtures';
import { customer, messages, products } from '../utils/testData';

test.describe('Cart & checkout', () => {
  test(
    'checkout without customer info should show a validation error',
    {
      tag: '@regression',
      annotation: { type: 'testcase', description: 'TC-CHK-001' },
    },
    async ({ loggedInInventory, cartPage, checkoutPage }) => {
      await loggedInInventory.addToCart(products.backpack.slug);
      await loggedInInventory.openCart();
      await cartPage.startCheckout();

      await checkoutPage.continue();

      await expect(checkoutPage.error).toBeVisible();
      await expect(checkoutPage.title).toHaveText('Checkout: Your Information');
    },
  );

  test(
    'a user can complete a purchase end to end',
    {
      tag: ['@smoke', '@regression'],
      annotation: { type: 'testcase', description: 'TC-CHK-002' },
    },
    async ({ loggedInInventory, cartPage, checkoutPage }) => {
      await test.step('Add a product and open the cart', async () => {
        await loggedInInventory.addToCart(products.backpack.slug);
        await loggedInInventory.openCart();
        await expect(cartPage.items).toHaveCount(1);
        expect(await cartPage.itemNames()).toContain(products.backpack.name);
      });

      await test.step('Enter customer information', async () => {
        await cartPage.startCheckout();
        await checkoutPage.fillCustomerInfo(customer);
        await checkoutPage.continue();
        await expect(checkoutPage.title).toHaveText('Checkout: Overview');
      });

      await test.step('Finish the order', async () => {
        await checkoutPage.finish();
        await expect(checkoutPage.completeHeader).toContainText(messages.orderComplete);
      });
    },
  );
});
