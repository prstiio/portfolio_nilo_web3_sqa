// Synthetic test data only. Credentials belong to a public demo site (or the local mock).
// NOTE: do not use the generic USERNAME env var (it collides with the OS user on Windows).

const password = process.env.SAUCE_PASSWORD ?? 'secret_sauce';

export const users = {
  standard: { username: process.env.SAUCE_USER ?? 'standard_user', password },
  lockedOut: { username: 'locked_out_user', password },
} as const;

export const products = {
  backpack: { slug: 'sauce-labs-backpack', name: 'Sauce Labs Backpack' },
  bikeLight: { slug: 'sauce-labs-bike-light', name: 'Sauce Labs Bike Light' },
  onesie: { slug: 'sauce-labs-onesie', name: 'Sauce Labs Onesie' },
} as const;

export const customer = {
  firstName: 'Test',
  lastName: 'Customer',
  postalCode: '12345',
} as const;

export const messages = {
  usernameRequired: /Username is required/i,
  passwordRequired: /Password is required/i,
  invalidCredentials: /do not match any user/i,
  lockedOut: /locked out/i,
  notLoggedIn: /when you are logged in/i,
  orderComplete: /Thank you for your order/i,
} as const;
