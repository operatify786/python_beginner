# Format Specifiers  .2f, 20, 040, < ,> ,^ , +,   , , , +,.2f,

burger = 500.567567567
pizza = 1500.78678678678
wings = 460.7867867843

print(f"Price of burger = Rs{burger:+,.2f}")
print(f"Price of pizza = Rs{pizza:+,.2f}")
print(f"Price of wings = Rs{wings:+,.2f}")