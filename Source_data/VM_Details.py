import paramiko

command = "df"

# Update the next three lines with your
# server's information

host = "10.0.0.255"
username = "nick"
password = 12345

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
_stdin, _stdout, _stderr = client.exec_command("df")
print(_stdout.read().decode())
client.close()
