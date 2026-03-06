"""
My Block Cipher with GCM Mode
CSI2108 Portfolio Assignment Part 1 - Question 2

Block size: 9 characters (72 bits)
Key: 9 characters
Core: Simple SPN (sub, perm, key add, 4 rounds + final)
Mode: GCM (Counter for confidentiality + simple GHASH for tag)

Run it, enter 9-char key, it encrypts + gives authentication tag
"""

def substitute(byte):
    """Simple substitution for nonlinearity"""
    return (byte * 5 + 13) % 256

def permute(state):
    """My permutation table for 9 bytes"""
    table = [5, 8, 2, 6, 0, 3, 7, 1, 4]
    return [state[i] for i in table]

def add_key(state, round_key):
    """XOR with round key"""
    return [s ^ k for s, k in zip(state, round_key)]

def make_round_keys(key):
    """Rotate key for 5 subkeys"""
    key_bytes = [ord(c) for c in key]
    round_keys = []
    current = key_bytes[:]
    for _ in range(5):
        round_keys.append(current[:])
        current = current[1:] + current[:1]
    return round_keys

def encrypt_block(block, round_keys):
    """Encrypt one 9-byte block (SPN)"""
    state = block[:]
    
    # 4 full rounds
    for r in range(4):
        state = add_key(state, round_keys[r])
        state = [substitute(b) for b in state]
        state = permute(state)
    
    # Final key addition
    state = add_key(state, round_keys[4])
    
    return state

# GCM part (simple educational version)
def inc_counter(counter):
    """Increment the last 4 bytes of counter"""
    ctr = bytearray(counter)
    i = 8  # last 4 bytes
    while i >= 5:  # nonce is first 5 bytes
        ctr[i] += 1
        if ctr[i] != 0:
            break
        i -= 1
    return bytes(ctr)

def simple_ghash(h, data):
    """Simple GHASH - XOR all blocks (educational, not full poly)"""
    g = 0
    for i in range(0, len(data), 9):
        block = data[i:i+9] + b'\x00' * (9 - len(data[i:i+9]))
        block_int = int.from_bytes(block, 'big')
        g ^= block_int
    return g.to_bytes(9, 'big')

def gcm_encrypt(message, key, nonce=b'\x00'*5):
    """GCM using my SPN (Counter mode + simple tag)"""
    round_keys = make_round_keys(key)
    
    # H = encrypt zero block
    h = bytes(encrypt_block([0]*9, round_keys))
    
    pt = message.encode()
    ct = bytearray()
    
    counter = nonce + b'\x00\x00\x00\x01'  # initial counter
    
    # Counter mode encryption
    for i in range(0, len(pt), 9):
        block = pt[i:i+9]
        pad = b'\x00' * (9 - len(block))
        full_block = block + pad
        
        # Encrypt counter
        ctr_block = list(counter)
        keystream = encrypt_block(ctr_block + [0]*(9-len(ctr_block)), round_keys)
        
        # XOR
        for j in range(len(full_block)):
            ct.append(full_block[j] ^ keystream[j])
        
        counter = inc_counter(counter)
    
    # Simple tag
    tag_input = bytes(ct) + len(message).to_bytes(4, 'big')
    tag = simple_ghash(h, tag_input)
    
    return bytes(ct), tag

# Main
if __name__ == "__main__":
    message = "Convert $502.89 AUD to 98283.04 LKR on 5 January 2026."
    
    print("My Block Cipher with GCM")
    print("Message:", message)
    
    key = input("\nEnter 9-character key: ")
    while len(key) != 9:
        print("Must be 9 characters!")
        key = input("Enter key: ")
    
    nonce = b'\xCA\xFE\xBA\xBE\x01'  # fixed for demo
    
    ciphertext, tag = gcm_encrypt(message, key, nonce)
    
    print("\nCiphertext (hex):")
    print(' '.join(f'{b:02X}' for b in ciphertext))
    
    print("\nAuthentication Tag (hex):")
    print(' '.join(f'{b:02X}' for b in tag))
    
    print("\nDone!")
