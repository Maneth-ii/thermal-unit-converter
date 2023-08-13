def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273
    return kelvin

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273
    return celsius

def main():
    F_or_C = input("Enter your conversion choice (e.g., 'F to C', 'C to F', 'C to K', 'K to C'): ")

    if F_or_C == "F to C":
        F = float(input("Enter Fahrenheit Value: "))
        C = fahrenheit_to_celsius(F)
        print(C, "Celsius")

    elif F_or_C == "C to F":
        C = float(input("Enter Celsius Value: "))
        F = celsius_to_fahrenheit(C)
        print(F, "Fahrenheit")

    elif F_or_C == "C to K":
        C = float(input("Enter Celsius Value: "))
        K = celsius_to_kelvin(C)
        print(K, "Kelvin")

    elif F_or_C == "K to C":
        K = float(input("Enter Kelvin Value: "))
        C = kelvin_to_celsius(K)
        print(C, "Celsius")

if __name__ == "__main__":
    main()
