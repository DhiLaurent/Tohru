# Tohru

![](/Tohruu.png?raw=true)

## PT-BR

Tohru é um script de Brute-Force em hashes /etc/shadow (SHA-512 crypt) do Linux 


## Como usar:

Python3 Tohru.py (WordList)

### Exemplo:

Hash Completa: $6$FJxnWBuM$KGY5W5wdIEL2mR8Jv5mcGPSKC6EPZW7Mruhqf5rZazegntdExwUcJoSqCzYrifutf6QoSRsyO0YQWxTTQo4yP1

Salt: (cifrão)6(cifão)FJxnWBuM(cifrão)

Após colocar os argumentos, o script irá solicitar se deseja esconder as tentativas de quebra de senha, caso sim ela rodara o script em background se não cada uma das tentativas sera mostrada na tela até o final da WordList ou a senha ser encontrada.

## EN-US

Tohru is a Brute-Force script to unhash /etc/shadow (SHA-512 crypt) password on Linux

## How to use:

## Cloning

````
$ git clone https://github.com/DhiLaurent/Tohru
````

````
$ python3 Tohru.py (WordList)
````

### Example:

Full Hash: $6$FJxnWBuM$KGY5W5wdIEL2mR8Jv5mcGPSKC6EPZW7Mruhqf5rZazegntdExwUcJoSqCzYrifutf6QoSRsyO0YQWxTTQo4yP1

Salt: (dollar sign)6(dollar sign)FJxnWBuM(dollar sign)

After putting arguments, Tohru will ask if you want to see her performing the attempts in real time, if not, type “Y”.

In case "art" module isn't installed, Tohru will do
