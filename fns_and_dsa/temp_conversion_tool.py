FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    try:
        temp = float(input("enter the temperature: "))
        unit = input("is the temp is celsius or fahrenheit (C/F)? ").strip().upper()


        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°F is equal to {converted_temp:.2f}°C")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°C is equal to {converted_temp:.2f}°F")
        else:
            print("invalid input.")
    except ValueError:
        return ValueError("invalid temprature. please enter a number.")
    
if __name__ == "__main__":
    main()

