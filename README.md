# Tohru

PT-BR

Tohru é um script de Brute-Force em hashes /etc/shadow do Linux 

[*] Necessário a instalação do módulo "art"

Comando: pip install art

Como usar:

Python3 Tohru.py (WordList)

Exemplo:

Hash Completa: $6$FJxnWBuM$KGY5W5wdIEL2mR8Jv5mcGPSKC6EPZW7Mruhqf5rZazegntdExwUcJoSqCzYrifutf6QoSRsyO0YQWxTTQo4yP1

Salt: $6$FJxnWBuM$

Após colocar os argumentos, o script irá solicitar se deseja esconder as tentativas de quebra de senha, caso sim ele rodara o script em background se não cada uma das tentativas sera mostrada na tela até o final da WordList ou a senha ser encontrada.

EN-US

Tohru is a Brute-Force script to unhash /etc/shadow password on Linux

[*] To script works is required install module "art"

Command: pip install art

How to use:

Python3 Tohru.py (WordList)

Example:

Full Hash: $6$FJxnWBuM$KGY5W5wdIEL2mR8Jv5mcGPSKC6EPZW7Mruhqf5rZazegntdExwUcJoSqCzYrifutf6QoSRsyO0YQWxTTQo4yP1

Salt: $6$FJxnWBuM$

After putting arguments, Tohru will request full hash and salt to break the password based in your Wordlist, in case Tohru can't break it, nothing returns.


