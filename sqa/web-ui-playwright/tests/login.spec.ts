import { test, expect } from '../fixtures';
import { messages, users } from '../utils/testData';

test.describe('Login', () => {
  test.beforeEach(async ({ loginPage }) => {
    await loginPage.goto();
  });

  test(
    'valid credentials should open the product list',
    {
      tag: '@smoke',
      annotation: { type: 'testcase', description: 'TC-LOGIN-001' },
    },
    async ({ loginPage, inventoryPage, page }) => {
      await loginPage.login(users.standard.username, users.standard.password);

      await expect(page).toHaveURL(/inventory/);
      await expect(inventoryPage.title).toHaveText('Products');
      await expect(inventoryPage.items.first()).toBeVisible();
    },
  );

  test(
    'wrong password should show an error and keep the user on the login page',
    {
      tag: '@regression',
      annotation: { type: 'testcase', description: 'TC-LOGIN-002' },
    },
    async ({ loginPage, page }) => {
      await loginPage.login(users.standard.username, 'not-the-password');

      await loginPage.expectError(messages.invalidCredentials);
      await expect(page).not.toHaveURL(/inventory/);
    },
  );

  test(
    'empty username should show a "username required" error',
    {
      tag: '@regression',
      annotation: { type: 'testcase', description: 'TC-LOGIN-003' },
    },
    async ({ loginPage }) => {
      await loginPage.password.fill(users.standard.password);
      await loginPage.loginButton.click();

      await loginPage.expectError(messages.usernameRequired);
    },
  );

  test(
    'empty password should show a "password required" error',
    {
      tag: '@regression',
      annotation: { type: 'testcase', description: 'TC-LOGIN-004' },
    },
    async ({ loginPage }) => {
      await loginPage.username.fill(users.standard.username);
      await loginPage.loginButton.click();

      await loginPage.expectError(messages.passwordRequired);
    },
  );

  test(
    'locked-out user should not be able to log in',
    {
      tag: '@regression',
      annotation: { type: 'testcase', description: 'TC-LOGIN-005' },
    },
    async ({ loginPage, page }) => {
      await loginPage.login(users.lockedOut.username, users.lockedOut.password);

      await loginPage.expectError(messages.lockedOut);
      await expect(page).not.toHaveURL(/inventory/);
    },
  );

  test(
    'opening the product page directly without logging in should be refused',
    {
      tag: '@regression',
      annotation: { type: 'testcase', description: 'TC-LOGIN-007' },
    },
    async ({ loginPage, inventoryPage, page }) => {
      await page.goto('/inventory.html');

      await loginPage.expectError(messages.notLoggedIn);
      await expect(inventoryPage.items).toHaveCount(0);
    },
  );
});
