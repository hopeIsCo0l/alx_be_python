# weather_advice.py

def main():
    # Prompt the user for the current weather condition
    weather = input("What's the weather like today? (sunny/rainy/cold): ").lower().strip()

    # Provide clothing recommendations based on the weather input
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        # print("Sorry, I don't have recommendations for this weather.")
if __name__ == "__main__":
    main()
