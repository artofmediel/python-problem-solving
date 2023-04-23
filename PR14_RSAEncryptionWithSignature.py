# This is a continuation of PR13_RSAEncryption.py

import rsa

# generate keys with length of 1024 bits
public_key, private_key = rsa.newkeys(1024)

# using the generated keys
with open("public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

# Sample encryption:
message = "Created new account on Twitter which is @madeupname12345"

# generate signature
#signature = rsa.sign(message.encode(), private_key, "SHA-256")  # SHA-256 is a hashing algorithm
#with open("signature", "wb") as f:
#    f.write(signature)

with open("signature", "rb") as f:
    signature = f.read()

# VerificationError: if you tamper the message
#message = "Created new account in GITHUB which is @madeupname12345"
# VerificationError: use new pair of keys , same message
#public_key, private_key = rsa.newkeys(1024)

# check if you get SHA-256
print(rsa.verify(message.encode(), signature, public_key))
# it mean that the message is authentic if you get SHA-256