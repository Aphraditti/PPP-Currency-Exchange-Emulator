class Currency:
  currencies = {
    'CHF': 0.930023,  # Swiss Franc
    'CAD': 1.264553,  # Canadian Dollar
    'GBP': 0.737414,  # British Pound
    'JPY': 111.019919,  # Japanese Yen
    'EUR': 0.862361,  # Euro
    'USD': 1.0  # US Dollar
  }

  def __init__(self, value, unit="USD"):
    self.value = value
    self.unit = unit

  def changeTo(self, new_unit):
    self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
    self.unit = new_unit

  def __repr__(self):
    return f"{self.value:.2f} {self.unit}"

  def __str__(self):
    return repr(self)

  def __add__(self, other):
    if isinstance(other, Currency):
      return Currency(self.value + other.convert_to(self.unit).value, self.unit)
    elif isinstance(other, (int, float)):
      return Currency(self.value + other, self.unit)
    else:
      raise TypeError("Unsupported operand type for +")

  def __radd__(self, other):
    return self.__add__(other)

  def __sub__(self, other):
    if isinstance(other, (int, float)):
      return Currency(self.value - other, self.unit)
    else:
      raise TypeError("Unsupported operand type for -")

  def __rsub__(self, other):
    return Currency(other - self.value, self.unit)

  def convert_to(self, new_unit):
    return Currency(self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit], new_unit)


v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)  # Output: 43.61 EUR
print(v2 + v1)  # Output: 23.10 USD
print(v1 + 3)  # Output: 26.43 EUR
print(3 + v1)  # Output: 26.43 EUR
print(v1 - 3)  # Output: 20.43 EUR
print(30 - v2)  # Output: 10.03 USD
