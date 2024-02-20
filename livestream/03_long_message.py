from enigma.machine import EnigmaMachine

machine = EnigmaMachine.from_key_sheet(
    rotors = "II V III",
    reflector= 'B',
    ring_settings='1 1 1',
    plugboard_settings="AV BS CG DL FU HZ IN KM OW RX"
)

machine.set_display('QJF')

def pad_string(input):
    padding_needed = (5 - len(input) % 5) % 5

    padding_string = input + "X" * padding_needed
    return padding_string

def format_for_transmission(input_string):

    return ' '.join(input_string[i:i+5] for i in range (0, len(input_string), 5))


plaintext = "HEY ROBOT MAKERS THIS IS A SECRET MESSAGE"
plaintext = plaintext.replace(" ", "X")
plaintext = pad_string(plaintext)

ciphertext = machine.process_text(plaintext)

print(format_for_transmission(ciphertext))