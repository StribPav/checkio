def recall_password(cipher_grille, ciphered_password):
    word = ''

    for i in range(4):
        for (keys, values) in zip(cipher_grille, ciphered_password):
            for (k, v) in zip(keys, values):
                if k == 'X':
                    word += v

        cipher_grille = tuple(zip(*cipher_grille[::-1]))

    return word
