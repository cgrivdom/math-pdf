from fpdf import FPDF
import random


class PDF(FPDF):

    def header(self):

        # Set font
        self.set_font("helvetica", "B", 15)

        # Move cursor to the right
        self.cell(80)

        # Print title
        self.cell(30, 10, "Here are your practice problems :)", align="C")

        # Perform a line break
        self.ln(20)


    def footer(self):

        # Position cursor at 1.5 cm from bottom
        self.set_y(-15)

        # Set font
        self.set_font("helvetica", "I", 8)

        # Print page number
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")


def main():

    while True:
    
        print("What would you like to practice today?")
        print("a -> Addition")
        print("s -> Substraction")
        print("m -> Multiplication")
        print("d -> Division")

        exercise = input()

        exercise = exercise.strip().lower()

        exercise = exercise[0]

        if exercise == "a" or exercise == "s" or exercise == "m" or exercise == "d":

            break
    
    if exercise == "a":
    
        pdf = PDF()

        pdf.add_page()

        pdf.set_font("Times", size=12)

        for i in range(40):

            pdf.cell(0, 10, f"{random.randint(1, 99)} + {random.randint(1, 99)} =", new_x="LMARGIN", new_y="NEXT", align="C")

        # Test generated string 
        addition = f"{random.randint(1, 99)} + {random.randint(1, 99)} ="

        valid_addition(addition)

        pdf.output("output.pdf")

    elif exercise == "s":

        pdf = PDF()

        pdf.add_page()

        pdf.set_font("Times", size=12)

        for i in range(40):

            pdf.cell(0, 10, f"{random.randint(1, 99)} - {random.randint(1, 99)} =", new_x="LMARGIN", new_y="NEXT", align="C")

        substraction = f"{random.randint(1, 99)} - {random.randint(1, 99)} ="

        valid_substraction(substraction)

        pdf.output("output.pdf")

    elif exercise == "m":

        pdf = PDF()

        pdf.add_page()

        pdf.set_font("Times", size=12)

        for i in range(40):

            pdf.cell(0, 10, f"{random.randint(1, 99)} x {random.randint(1, 99)} =", new_x="LMARGIN", new_y="NEXT", align="C")

        multiplication = f"{random.randint(1, 99)} x {random.randint(1, 99)} ="

        valid_multiplication(multiplication)
        
        pdf.output("output.pdf")

    elif exercise == "d":

        pdf = PDF()

        pdf.add_page()

        pdf.set_font("Times", size=12)

        for i in range(40):

            pdf.cell(0, 10, f"{random.randint(1, 99)} / {random.randint(1, 99)} =", new_x="LMARGIN", new_y="NEXT", align="C")

        division = f"{random.randint(1, 99)} / {random.randint(1, 99)} ="

        valid_division(division)
        
        pdf.output("output.pdf")


def valid_addition(addition):

    x, y = addition.split("+")

    x = x.strip()
    y = y.replace("=", "").strip()

    if x.isnumeric() == True and y.isnumeric() == True:

        return True
    
    else:

        return False


def valid_substraction(substraction):

    x, y = substraction.split("-")

    x = x.strip()
    y = y.replace("=", "").strip()

    if x.isnumeric() == True and y.isnumeric() == True:

        return True
    
    else:

        return False


def valid_multiplication(multiplication):

    x, y = multiplication.split("x")

    x = x.strip()
    y = y.replace("=", "").strip()

    if x.isnumeric() == True and y.isnumeric() == True:

        return True
    
    else:

        return False


def valid_division(division):

    x, y = division.split("/")

    x = x.strip()
    y = y.replace("=", "").strip()

    if x.isnumeric() == True and y.isnumeric() == True:

        return True
    
    else:

        return False        


if __name__ == "__main__":
    main()