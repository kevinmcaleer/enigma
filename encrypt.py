from enigma.machine import EnigmaMachine

machine = EnigmaMachine.from_key_sheet(
   rotors='IV I V',
   reflector='B',
   ring_settings='20 5 10',
   plugboard_settings='SX KU QP VN JG TC LA WM OB ZF')

# Set the initial position of the Enigma rotors
machine.set_display('BFR')

# Encrypt the text 'BFR' and store it as msg_key
# msg_key = machine.process_text('BFR')
# print(msg_key)
plaintext = 'RASPBERRYPI'
ciphertext = machine.process_text(plaintext)
print(ciphertext)

