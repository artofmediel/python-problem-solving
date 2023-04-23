import rsa

# generate keys with length of 1024 bits
public_key, private_key = rsa.newkeys(1024)

# generate public and private keys
#with open("public.pem", "rb") as f:
#    f.write(public_key.save_pkcs1("PEM"))

#with open("private.pem", "wb") as f:
#    f.write(private_key.save_pkcs1("PEM"))

# using the generated keys
with open("public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

# Sample encryption:
message = "Hello, my password is testpassword123"

# encrypt the message with the public key
#encrypted_message = rsa.encrypt(message.encode(), public_key)
# check
#print(encrypted_message)

# make a file : encrypted.message
#with open("encrypted.message", "wb") as f: # wb is write byte
#    f.write(encrypted_message)

# open encrypted file
encrypted_message = open("encrypted.message", "rb").read()  # rb is read byte
# decrypt using private key
clear_message = rsa.decrypt(encrypted_message, private_key)
# check
print(clear_message.decode())
