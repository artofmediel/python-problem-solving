import string
import numpy as np
from egcd import egcd # pip install egcd

alphabet = 'abcdefghijklmnopqrstuvwxyz'

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

def matrix_mod_inv(matrix, modulus):
    ''' We find the matrix modulus inverse by
    Step 1) Find determinant
    Step 2) Find the inverse of the determinant value in modulus
            in a specific modulus (usually length of alphabet)
    Step 3) Take that det_inv times the det*inverted matrix in
            modulus 26 (applied elementwise)
    '''

    det = int(np.round(np.linalg.det(matrix))) # step 1
    det_inv = egcd(det, modulus)[1] % modulus # step 2
    matrix_modulus_inv = det_inv * np.round(det*np.linalg.inv(matrix)).astype(int) % modulus # step 3

    return matrix_modulus_inv

def encrypt(message, K):
    encrypted = ''
    message_in_numbers = []

    # make message into numbers
    for letter in message:
        message_in_numbers.append(letter_to_index[letter])

    # split into the size of matrix K
    split_P = [message_in_numbers[i:i+int(K.shape[0])] for i in range(0, len(message_in_numbers), int(K.shape[0]))]

    # iterate through each partial message and encrypt is using K*P (mod 26)
    for P in split_P:
        P = np.transpose(np.asarray(P))[:, np.newaxis]

        while P.shape[0] != K.shape[0]:
            P = np.append(P, letter_to_index['x'])[:, np.newaxis]

        numbers = np.dot(K,P) % len(alphabet)

        n = numbers.shape[0]

        # map it back to text

        for idx in range(n):
            number = int(numbers[idx, 0])
            encrypted += index_to_letter[number]

    return encrypted

def decrypt(cipher, Kinv):
    decrypted = ''
    cipher_in_numbers = []

    # make cipher text into numbers
    for letter in cipher:
        cipher_in_numbers.append(letter_to_index[letter])

    # split it into the size of matrix inv(K) so we can do the matrix mult.
    split_C = [cipher_in_numbers[i:i + int(Kinv.shape[0])] for i in range(0, len(cipher_in_numbers), int(Kinv.shape[0]))]

    # iterate through each partial cipher text and decrypt using inv(K)*C (mod 26)
    for c in split_C:
        c = np.transpose(np.asarray(c))[:, np.newaxis]
        numbers = np.dot(Kinv, c) % len(alphabet)
        n = numbers.shape[0]

        # Map back number to decrypted text
        for idx in range(n):
            number = int(numbers[idx, 0])
            decrypted += index_to_letter[number]

    return decrypted

def main():
    K = np.array([[3,3],[2,5]])
    message = input("Enter message : ")
    message = message.lower()
    print("Message : " + message)
    valid_text = True

    for i in message:
        if i in string.ascii_lowercase:
            valid_text = True
        else:
            valid_text = False

    if valid_text == True:
        passed(message, K)
    else:
        print("Numbers and special characters are invalid.")


def passed(message, K):
    encrypted_message = encrypt(message, K)
    # check
    print("Encrypted : " + encrypted_message)

    Kinv = matrix_mod_inv(K, len(alphabet))

    decrypted_message = decrypt(encrypted_message, Kinv)
    # check
    print("Decryption test : " + decrypted_message)

main()