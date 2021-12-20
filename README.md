# Tohru

PT-BR

Tohru é um script de Brute-Force em hashes /etc/shadow do Linux 

Como usar:

Python3 Tohru.py (WordList)

Exemplo:

Hash Completa: $6$FJxnWBuM$KGY5W5wdIEL2mR8Jv5mcGPSKC6EPZW7Mruhqf5rZazegntdExwUcJoSqCzYrifutf6QoSRsyO0YQWxTTQo4yP1

Salt: $6$FJxnWBuM$

Após colocar os argumentos, o script irá solicitar a Hash completa e Salt para tentar quebrar a senha baseado na WordList, caso não consiga não irá retornar nada.

EN-US

Tohru is a Brute-Force script to unhash etc/shadow password on Linux

How to use:

Python3 Tohru.py (WordList)

Example:

Full Hash: $6$FJxnWBuM$KGY5W5wdIEL2mR8Jv5mcGPSKC6EPZW7Mruhqf5rZazegntdExwUcJoSqCzYrifutf6QoSRsyO0YQWxTTQo4yP1

Salt: $6$FJxnWBuM$

After putting arguments, Tohru will request full hash and salt to break the password based in your Wordlist, in case Tohru can't break it, nothing returns.


