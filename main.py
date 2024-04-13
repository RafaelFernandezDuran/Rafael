class MaximoDivisorComun:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calcular_mcd(self):
        a = self.num1
        b = self.num2
        while b:
            a, b = b, a % b
        return a

def main():
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))

        if num1 <= 0 or num2 <= 0:
            print("Por favor ingrese números enteros positivos.")
            return

        mdc_calculator = MaximoDivisorComun(num1, num2)
        mcd = mdc_calculator.calcular_mcd()
        print(f"El máximo común divisor de {num1} y {num2} es: {mcd}")

    except ValueError:
        print("Por favor ingrese números enteros válidos.")

if __name__ == "__main__":
    main()
