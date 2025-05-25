import argparse




def resistor_value():


    parser = argparse.ArgumentParser(description="Determine the Resistor Value")


    parser.add_argument("-d1","--digit1",type=str, required=True, help="Color of 1st Band")
    parser.add_argument("-d2","--digit2",type=str, required=True, help="Color of 2nd Band")
    parser.add_argument("-d3","--digit3",type=str, required=True, help="Color of 3rd Band")
    parser.add_argument("-m","--multiplier",type=str, required=True, help="Color of Multiplier Band")
    parser.add_argument("-t","--tolerance",type=str, required=True, help="Color of Tolerance Band")

    choice = parser.parse_args()
    resistor_val=""

    multiplier_dict = {
        "black": "1",
        "brown": "10^1",
        "red": "10^2",
        "orange": "10^2",
        "yellow": "10^2",
        "green": "10^2",
        "blue": "10^2",
        "violet": "10^2",
        "grey": "10^2",
        "white": "10^9",
        "gold": "0.1",
        "silver": "0.01"
    }



    digit_dict={
        "black":0,
        "brown":1,
        "red":2,
        "orange":3,
        "yellow":4,
        "green":5,
        "blue":6,
        "violet":7,
        "grey":8,
        "white":9
    }



    if choice.digit1.lower() in digit_dict.keys():
        resistor_val+=str(digit_dict[choice.digit1.lower()])
    else:
        print("Incorrect Digit Color, Please check the color again.")

    if choice.digit2.lower() in digit_dict.keys():
        resistor_val+=str(digit_dict[choice.digit2.lower()])
    else:
        print("Incorrect Digit Color, Please check the color again.")

    if choice.digit3.lower() in digit_dict.keys():
        resistor_val+=str(digit_dict[choice.digit2.lower()])
    else:
        print("Incorrect Digit Color, Please check the color again.")

    if choice.multiplier.lower() in multiplier_dict.keys() and multiplier_dict[choice.multiplier.lower()] != "1":
        resistor_val+="*"+multiplier_dict[choice.multiplier]
    else:
        print("Incorrect Multiplier Color, Please check the color again.")


    if choice.tolerance.lower() == "brown":
        resistor_val+=" +/- 2%"
    elif choice.tolerance.lower() == "red":
        resistor_val+=" +/- 10%"
    elif choice.tolerance.lower() == "gold":
        resistor_val+=" +/- 5%"
    elif choice.tolerance.lower() == "silver":
        resistor_val+=" +/- 10%"
    else:
        print("Incorrect Tolerance Color, Please check the color again.")



    print(f"The resistor value is {resistor_val} ohms")

    input("Press Enter to Exit......")


if __name__== '__main__':
    resistor_value()
