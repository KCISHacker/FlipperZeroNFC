import json
import os

with open(input("Data file path: "), 'r', encoding='utf-8') as file:
    data = json.load(file)
    file.close()

print("Loaded file, last updated: " + data["last_update"])
print("Obj count: " + str(data["count"]))

if not os.path.exists('outputs'):
    os.makedirs('outputs')

def convert_to_hex_id(card_id):
    hex_str = hex(card_id)[2:].zfill(8).upper()
    hex_segments = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]
    output = ' '.join(reversed(hex_segments))
    return output

for obj in data["data"]:
    str_id = str(obj['id'])
    card_id = int(obj['card_id'])
    hex_id = convert_to_hex_id(card_id)
    print('Store ' + str_id + ' with id ' + hex_id)
    with open('outputs/' + str_id + ".nfc", 'w') as file:
        file.write('''Filetype: Flipper NFC device
Version: 4
# Device type can be ISO14443-3A, ISO14443-3B, ISO14443-4A, ISO14443-4B, ISO15693-3, FeliCa, NTAG/Ultralight, Mifare Classic, Mifare DESFire, SLIX, ST25TB
Device type: Mifare Classic
# UID is common for all formats
UID: {id}
# ISO14443-3A specific data
ATQA: 00 04
SAK: 08
# Mifare Classic specific data
Mifare Classic type: 1K
Data format version: 2
# Mifare Classic blocks, '??' means unknown data
Block 0: {id} EB 08 04 00 04 71 45 E7 CF 66 60 90
Block 1: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 2: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 3: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 4: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 5: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 6: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 7: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 8: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 9: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 11: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 12: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 13: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 14: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 15: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 16: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 17: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 18: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 19: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 21: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 22: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 23: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 24: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 25: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 26: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 27: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 28: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 29: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 31: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 32: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 33: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 34: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 35: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 36: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 37: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 38: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 39: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 41: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 42: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 43: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 44: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 45: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 46: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 47: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 48: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 49: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 51: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 52: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 53: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 54: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 55: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 56: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 57: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 58: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 59: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 61: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 62: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 63: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
'''.format(id = hex_id))
    file.close()