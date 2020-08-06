
end = '\n'
import env, os, time

if env.getEnvVariable('user') == 'guest':
	os.system('bash config.sh')
bootime = 0
if env.getEnvVariable('shortboot'):
	bootime = 3
else:
	bootime = 6

for i in range(bootime):
	print("Booting." + '.'*((i+1)%3))
	time.sleep(1)
	os.system('clear')
print("\033[1mWelcome to TophatCMD \033[36mAlpha 1.0\033[0m")
print("Type 'help' for help")
print("Type 'terminal' to enter the shell")
print("Type 'exit' to exit the shell")
while True:
	command = input('>>> ')
	if command == 'help':
		print("Type 'help' for help")
		print("Type 'terminal' to enter the shell")
		print("Type 'exit' to exit the shell")
		print("Type 'bash' to run a bash script from a file")
	elif command == 'terminal':
		exec(compile(open('shell.py', 'r').read(), 'code.py', 'exec'))
	elif command == 'vi':
		os.system('vi')
	elif command[0:5] == 'bash ':
		os.system('bash ') 
	elif command == 'reboot':
		os.system('bash main.sh')