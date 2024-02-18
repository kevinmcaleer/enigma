from bruteforce_octapi import find_rotor_start, rotors

ciphertext = "FKFPQZYVON"
cribtext = "CHELTENHAM"
ring_choice = "1 1 1"

found = False
for rotor_choice in rotors:
    rotor_setting, ring_setting, start_pos = find_rotor_start(rotor_choice, ring_choice, ciphertext, cribtext)

    if start_pos != "Cannot find settings":
        found = True
        print( "Rotors %s, ring %s, message key was %s, using crib %s" % (rotor_setting, ring_setting, start_pos, cribtext) )

if found == False:
    print( 'Attack unsuccessful' )
