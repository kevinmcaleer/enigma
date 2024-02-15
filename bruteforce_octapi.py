import dispy, socket

rotors = [ "I II III", "I II IV", "I II V", "I III II",
"I III IV", "I III V", "I IV II", "I IV III",
"I IV V", "I V II", "I V III", "I V IV",
"II I III", "II I IV", "II I V", "II III I",
"II III IV", "II III V", "II IV I", "II IV III",
"II IV V", "II V I", "II V III", "II V IV",
"III I II", "III I IV", "III I V", "III II I",
"III II IV", "III II V", "III IV I", "III IV II",
"III IV V", "IV I II", "IV I III", "IV I V",
"IV II I", "IV II III", "IV I V", "IV II I",
"IV II III", "IV II V", "IV III I", "IV III II",
"IV III V", "IV V I", "IV V II", "IV V III",
"V I II", "V I III", "V I IV", "V II I",
"V II III", "V II IV", "V III I", "V III II",
"V III IV", "V IV I", "V IV II", "V IV III" ]

def find_rotor_start(rotor_choice, cipher_text, crib_text, ring_choice):
    from enigma.machine import EnigmaMachine

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    machine = EnigmaMachine.from_key_sheet(
    rotors=rotor_choice,
    reflector='B', 
    ring_settings=ring_choice,
    )

    for rotor1 in alphabet:
        for rotor2 in alphabet:
            for rotor3 in alphabet:
                
                # Generate a possible start position
                start_pos = rotor1 + rotor2 + rotor3
                
                # Set the start position
                machine.set_display(start_pos)

                # Attempt to decrypt the plaintext
                plaintext = machine.process_text(cipher_text)
                print(plaintext)
                if plaintext == crib_text:
                    print("Valid settings found!")
                    print(rotor_choice, start_pos)
                    return rotor_choice, ring_choice, start_pos
         
    # If no valid settings are found, return None
    return rotor_choice, "Cannot find settings"

# Enter ciphertext, cribtext and ring choice
# ciphertext = input("Enter the ciphertext: ")
# cribtext = input("Enter the cribtext: ")
# ring_choice = input("Enter the ring choice: ")

ciphertext = "FKFPQZYVON"
cribtext = "CHELTENHAM"
ring_choice = "1 1 1"


cluster = dispy.JobCluster(find_rotor_start, nodes=['192.168.2.1','192.168.2.2'], loglevel=dispy.logger.DEBUG)
print(f" cluster status {cluster.status()}")

jobs = []
id = 1
# Submit the jobs for this ring choice
for rotor_choice in rotors:
    job = cluster.submit( rotor_choice, ciphertext, cribtext, ring_choice )
    job.id = id # Associate an ID to the job
    jobs.append(job)
    id += 1   # Next job

print( "Waiting..." )
cluster.wait()
print( "Collecting job results" )

# Collect and check through the jobs for this ring setting
found = False
for job in jobs:
    # Wait for job to finish and return results
    rotor_setting, ring_setting, start_pos = job()

    # If a start position was found
    if start_pos != "Cannot find settings":
        found = True
        print( "Rotors %s, ring %s, message key was %s, using crib %s" % (rotor_setting, ring_setting, start_pos, cribtext) )

if found == False:
    print( 'Attack unsuccessful' )

cluster.print_status()
cluster.close()