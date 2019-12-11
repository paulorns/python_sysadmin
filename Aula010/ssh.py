import paramiko

client = paramiko.client.SSHClient()

client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('127.0.0.1',username='developer',password='4linux')

# Standard input, Standard output, stardard error
stdin,stdout,stderr = client.exec_command('read VARIAVEL \n echo $VARIAVEL')

stdin.write('Xablau\n')
stdin.flush()

# if stdout.channel.recv_exit_status() == 0:
#     print('Saida padrao\n')
print(stdout.read().decode('utf-8'))
# else:
#     print('Saida de erro\n')
#     print(stderr.read().decode('utf-8'))

