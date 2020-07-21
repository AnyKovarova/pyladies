from random import randrange

def evaluate (string):
    if 'ooo' in string:
        return "o"
    if 'xxx' in string:
        return "x"
    elif '-' not in string:
        return "!"
    else:
        return "-"
    
def move(string, num_field, symbol):
    "Vypíše herní políčko s daným symbolem v něm."
    field_position = int(num_field)
    new_string = string[:(field_position-1)] + symbol + string[field_position:]
    return new_string

def player_move(string, num_field):
    "Podle tahu hráče vypíše změnu políčka"
    while True:
        if num_field.isdigit():
            field_position = int(num_field)
            if field_position >= 1 and field_position <= 20:
                if string[(field_position-1)] == '-':
                    new_string = string[:(field_position-1)] + 'x' + string[field_position:]
                    return new_string
                else:
                    num_field = input('Pozice musí být číslo: ')
            else:
                num_field = input('Pozice musí být číslo od 1 do 20: ')    
        else:
            num_field = input('Pozice musí být volná: ')

def comp_move(string, field_position):
    "Vypíše pole s tahem PC (náhodné)"
    while True:
        if string[(field_position-1)] == '-':
            new_string = string[:(field_position-1)] + 'o' + string[field_position:]
            return new_string
        else:
            field_position = randrange(1, 21)
            

def piskvorky(string):
    while True:
        if evaluate(string) == '-':
            string_player = player_move(string, input('Zadej pozici, na kterou chceš přejít: '))
            print(string_player)
            if evaluate(string_player) == '-':
                string_comp = comp_move(string_player, randrange(1, 21))
                print(string_comp)
                string = string_comp
            else:
                return evaluate(string_player)
        else:
            return evaluate(string)

print(piskvorky('--------------------'))