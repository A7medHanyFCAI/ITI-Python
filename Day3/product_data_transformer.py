import json

def check_valid_product_name(products):
    for x in products.split(","):
            if not x.strip() or not x.strip().isalnum():
                return True
    return False
    
def product_data_transformer():
    filename = "products.json"

    products = input("Enter product names (comma-separated): ").strip()
    flag = check_valid_product_name(products)
    while flag:
        print("Please enter valid product names.")
        products = input("Enter product names (comma-separated): ").strip()
        flag = check_valid_product_name(products)

    product_names = [x.strip() for x in products.split(",") if x.strip()]


    while True:
        prices_input = input("Enter product prices (comma-separated): ").strip()
        try:
            product_prices = [float(x) for x in prices_input.split(",") if x.strip()]
            if len(product_prices) != len(product_names):
                print(f"You entered {len(product_names)} names but {len(product_prices)} prices. Try again.")
                continue
            break
        except ValueError:
            print("Invalid price input.")

    
    paired = zip(product_names, product_prices)

    
    valid_products = filter(lambda x: x[1] > 0, paired)

    
    transformed = list(map(lambda x: {
        "product": x[0],
        "price": x[1],
        "discounted": round(x[1] * 0.9, 2)
    }, valid_products))

    
    with open(filename, "w") as f:
        json.dump(transformed, f, indent=4)

    # Show preview
    print(f"\n'{filename}' created with {len(transformed)} valid products.")
    print("\nPreview (first 5 results):")
    for item in transformed[:5]:
        print(item)


if __name__ == "__main__":
    product_data_transformer()
