/** Convert a price label like "$29.99" to a number. */
export function parsePrice(label: string): number {
  const value = Number(label.replace(/[^0-9.]/g, ''));
  if (Number.isNaN(value)) {
    throw new Error(`Cannot parse price from "${label}"`);
  }
  return value;
}

/** True when the array is sorted ascending (or descending) according to the comparer. */
export function isSorted<T>(
  items: T[],
  direction: 'asc' | 'desc',
  compare: (a: T, b: T) => number,
): boolean {
  return items.every((item, i) => {
    if (i === 0) return true;
    const result = compare(items[i - 1], item);
    return direction === 'asc' ? result <= 0 : result >= 0;
  });
}
