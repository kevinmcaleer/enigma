from enigma.machine import EnigmaMachine

machine = EnigmaMachine.from_key_sheet(
   rotors='II V III',
   reflector='B',
   ring_settings='1 1 1',
   plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')

machine.set_display('UYT')


message_key = machine.process_text('PWE')
print(message_key)

machine.set_display(message_key)

ciphertext = 'YJPYITREDSYUPIU'

plaintext = machine.process_text(ciphertext)
print(plaintext)