# Simple House Price Estimator

# Data: [Square Feet, Price]
houses = [
    {"sqft": 1000, "price": 100000},
    {"sqft": 1500, "price": 150000},
    {"sqft": 2000, "price": 200000},
]


def estimate_price(sqft):
    # Basic logic: $100 per square foot
    return sqft * 100


# Test the model
area = 1200
predicted_price = estimate_price(area)

print(f"House Size: {area} sqft")
print(f"Estimated Price: ${predicted_price}")