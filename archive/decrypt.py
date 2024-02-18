from enigma.machine import EnigmaMachine

machine = EnigmaMachine.from_key_sheet(
   rotors='II V III',
   reflector='B',
   ring_settings='1 1 1',
   plugboard_settings='AV BS CG DL FU HZ IN KM OW RX',
   )

MESSAGE = "SUPSH GPYCV JTPYF TDQWV HIBEW FPDBN TAUEL IQXMS ZBDCT"

# Set the initial position of the Enigma rotors
machine.set_display('QJF')

ciphertext = 'FKFPQZYVON'
crib = "ROBOT"

plaintext = machine.process_text(ciphertext)
print(plaintext)
print(plaintext.replace("X", " "))