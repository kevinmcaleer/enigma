from enigma.machine import EnigmaMachine

machine = EnigmaMachine.from_key_sheet(
   rotors='II V III',
#    reflector='B',
   ring_settings='1 1 1',
#    plugboard_settings='SX KU QP VN JG TC LA WM OB ZF'
   plugboard_settings='AV BS CG DL FU HZ IN KM OW RX',
   )

# Set the initial position of the Enigma rotors
machine.set_display('QJF')

# Encrypt the text 'BFR' and store it as msg_key
# msg_key = machine.process_text('QJF')
# print(msg_key)
plaintext = 'CHELTENHAM'
ciphertext = machine.process_text(plaintext)
print(ciphertext)

