import paramiko
# you can use either pem or id_rsa file
k = paramiko.RSAKey.from_private_key_file("/Users/whatever/Downloads/mykey.pem")
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("Connecting")
c.connect( hostname = "www.acme.com", username = "ubuntu", pkey = k )
print("Connected...")
commands = [ "/home/ubuntu/firstscript.sh", "/home/ubuntu/secondscript.sh" ]
for command in commands:
	print("Executing {}".format( command ))
	stdin , stdout, stderr = c.exec_command(command)
	print(stdout.read())
	print("Errors")
	print(stderr.read())
c.close()