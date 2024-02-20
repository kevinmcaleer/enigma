from enigma.machine import EnigmaMachine

machine = EnigmaMachine.from_key_sheet(
    rotors = "II V III",
    reflector= 'B',
    ring_settings='1 1 1',
    plugboard_settings="AV BS CG DL FU HZ IN KM OW RX"
)

machine.set_display('QJF')

ciphertext = 'FKFPQZYVON'
plaintext = machine.process_text(ciphertext)

print(plaintext)