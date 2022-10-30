# Tohru

![](/Tohru.png?raw=true)

Obs: Ainda será feito um PDF com imagens :)

# PT-BR

Tohru é um script de Brute-Force em hashes /etc/shadow do Linux 

[*] Necessário a instalação do módulo "art"

Comando: pip install art

# Como usar:

Python3 Tohru.py (WordList)

# Exemplo:

Hash Completa: $6$FJxnWBuM$KGY5W5wdIEL2mR8Jv5mcGPSKC6EPZW7Mruhqf5rZazegntdExwUcJoSqCzYrifutf6QoSRsyO0YQWxTTQo4yP1

Salt: (cifrão)6(cifrão) (cifão)FJxnWBuM(cifrão)

Após colocar os argumentos, o script irá solicitar se deseja esconder as tentativas de quebra de senha, caso sim ela rodara o script em background se não cada uma das tentativas sera mostrada na tela até o final da WordList ou a senha ser encontrada.

Obs: Infelizmente até o momento Tohru não consegue encontrar a senha caso i	dentifique que a Wordlist tenha um espaço em branco noo meio dela :c 

Comando: sed '/^$/d' arquivoantigo.txt > arquivonovo.txt 

# EN-US

Tohru is a Brute-Force script to unhash /etc/shadow password on Linux

[*] To script works is required install module "art"

Command: pip install art

# How to use:

Python3 Tohru.py (WordList)

# Example:

Full Hash: $6$FJxnWBuM$KGY5W5wdIEL2mR8Jv5mcGPSKC6EPZW7Mruhqf5rZazegntdExwUcJoSqCzYrifutf6QoSRsyO0YQWxTTQo4yP1

Salt: (dollar sign)6(dollar sign)FJxnWBuM(dollar sign) \$6\$FJxnWBuM$

After putting arguments, Tohru will ask if you want to see her performing the attempts in real time, if not, type “Y”.

Obs: Unfortunately until this moment Tohru can't find the password if have a blank line in the middle of wordlist :c, but if you use sed command you can’ “fix” it 

Command: sed '/^$/d' oldfile.txt > newfile.txt 

