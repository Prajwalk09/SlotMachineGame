"""A slot machine where users can bet a sum of money on a particular line (out of lines 1, 2 and 3). If a user wins the
bet,the bet amount will be multiplied with the number on the line and returned to the user. The user can continue
playing until he/she has money or runs out of money. """

import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3
"""Used to generate the slot machine"""
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
"""Used to assign the winnings of the user, incase he/she wins the bet they made."""
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    """The below for loop is used to get the first symbol at each row (columns[0])"""
    winnings = 0
    winning_lines =[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line+1)
    return winnings, winning_lines


"""A B C
   D E D
   F G H"""


def deposit():
    while True:
        amount = input("What would you like to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")
    return amount


def get_number_of_lines():
    """This function gets the number of lines on which the user wants to bet on"""
    while True:
        lines = input(f"Enter the number of lines to bet on 1 - {str(MAX_LINES)}? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number")
    return lines


def get_bet():
    """This function gets the amount each user wants to bet on each line"""
    while True:
        bet = input(f"What would you like to bet on each line? ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between {MIN_BET} and {MAX_BET}")
        else:
            print("Please enter a number")
    return bet


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    """Appending the symbols to the all_symbols list, as many times as their count"""
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    """Each nested list represents the value present in each column"""
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    """Used to display the elements of the column"""
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print("")


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Insufficient balance to bet that amount. Your current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines: ", *winnings_lines)
    return winnings - total_bet


def main():
    """main function is executed again, if the user wants to play again"""
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press Enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You are left with ${balance}")


main()


