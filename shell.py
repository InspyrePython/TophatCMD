def run(command, intmem):
	ID = hex(random.randint(0, 2**16))
	intmem = 0.000
	mem = []
	direct = str()
	filename = None
	dopen = False
	red = '\b\033[31m\033[1m'
	green = '\b\033[32m\033[1m'
	yellow = '\b\033[33m\033[1m'
	history = list()
	if direct == str():
		command = input(f'{yellow}shell> \033[0m')
	else:
		command = input(f'{yellow}shell/{direct}> \033[0m')
	command = command.replace('$', '')
	if command == 'cd':
		direct = str()
	elif command[0:3] == 'cd ':
		if direct == None:
			direct = str()
		else:
			try:
				if direct == str():
					inpec = command[3:len(command)]
					a = open(inpec, 'r')
				else:
					a = open(direct, 'r')
			except IsADirectoryError:
				if direct == str():
					direct += command[3:len(command)] + '/'
				else:
					direct += command[3:len(command)] + '/'
			except FileNotFoundError:
				print(red, 'Directory not found.')
	elif command[0:3] == 'rm ':
		try:
			try:
				os.remove(direct + command[3:len(command)])
				print(green, f'Deleted file {command[3:len(command)]}')
			except FileNotFoundError:
				print(red, f'{direct}{command[3:len(command)]} not found.')
		except IsADirectoryError:
			for item in os.listdir(direct + command[3:len(command)]):
				os.remove(direct + command[3:len(command)] + '/' + item)
			os.rmdir(direct + command[3:len(command)])
			print(green, f'Deleted directory {direct}{command[3:len(command)]}/{item}')
		except FileNotFoundError:
			print(red, f'{direct}{command[3:len(command)]} not found.')
	elif command[0:5] == 'read ':
		print(open(direct + command[5:len(command)], 'r').read())
	elif command == 'dir':
		try:
			contents = os.listdir(direct)
			for filename in contents:
				size = os.path.getsize(f'{direct}{filename}')
				if size in range(0, 1000):
					size = '| ' + str(size) + ' bytes'
				elif size in range(1000, 1000000):
					size = '| ' + str(size) + ' KB'
				elif size in range(1000000, 1000000000):
					size = '| ' + str(size) + ' MB'
				print(filename, size)
		except FileNotFoundError:
			print(red, f'Directory {direct} not found.')
	elif command[0:7] == 'python ':
		print(yellow, f'Executing file {command[7:len(command)]}...')
		try:
			exec(compile(open(direct + command[7:len(command)], 'r').read(), 'code.py', 'exec'))
		except FileNotFoundError:
			print(red, f'File {command[7:len(command)]} not found')
		except:
			print(red, 'Python file returned an error')
	elif command[0:7] == 'unpack ':
		try:
			a = zipfile.ZipFile(direct + command[7:len(command)])
			os.mkdir(command[7:len(command) - 4])
			a.extractall(command[7:len(command) - 4])
			print(green, f'Unpacked file {command[7:len(command)]}')
		except FileNotFoundError:
			print(red, f'File {command[7:len(command)]} not found')
	elif command[0:5] == 'echo ':
		print(command[5:len(command)])
	elif command[0:3] == 'dc ':
		try:
			exec(compile('print(' + command[3:len(command)] + ')', 'code.py', 'exec'))
		except ValueError:
			pass
	elif command == 'pwd':
		print(direct)
	elif command == 'uname':
		print(os.uname()[0])
	elif command == 'history':
		print("--------------------------------------------------")
		print("|       Command        |       Timestamp         |")
		print("--------------------------------------------------")
		for item in history:
			print(f"|  {item[0]}  " + " "*(18 - len(item[0])) + f"|    {item[1]}" + " "*(15 - len(str(item[1]))) + '   |')
			print("--------------------------------------------------")
	elif command == 'time':
		today = datetime.datetime.now()
		today = today.strftime("%I:%M:%S %p")
		print(today)
	elif command[0:7] == 'mkfile ':
		b = open(command[7:len(command)], 'w+')
	elif command[0:6] == 'mkdir ':
		os.mkdir(command[6:len(command)])
	elif command[0:5] == 'fmem ':
		try:
			a = open(direct + command[5:len(command)])
			mem.append(command[5:len(command)])
			print(green, f"Added {command[5:len(command)]} to memory.")
			intmem += int('0.00' + str(len(command[5:len(command)]))/10)
		except IsADirectoryError:
			print(red, f"{command[5:len(command)]} is a directory, not a file. Use 'dirmem' instead.")
		except FileNotFoundError:
			print(red, f"File {command[5:len(command)]} not found.")
	elif command[0:7] == 'dirmem ':
		try:
			if os.path.isfile(command[7:len(command)]):
				print(red, f"{command[7:len(command)]} is a file, not a directory. Use 'fmem' instead.")
			else:
				mem.append(command[7:len(command)])
				print(green, f"Added {command[7:len(command)]} to memory.")
				intmem += int('0.00' + str(len(command[7:len(command)]))/10)
		except FileNotFoundError:
			print(red, f"Directory {command[7:len(command)]} not found.")
	elif command[0:5] == 'cmem ':
		mem.append(command[5:len(command)])
		intmem += int('0.00' + str(len(command[5:len(command)]))/10)
	elif command == 'mem':
		print("Memory: ", *mem, )
	elif command == 'flmem':
		mem.remove(mem[len(mem) - 1])
		print(green, f"Removed value '{mem[len(mem) - 1]}' from memory")
		intmem -= int('0.00' + str(len(len(mem[len(mem) - 1]))/10))
	elif command == 'dmem':
		print(f"Deleted {len(mem)} items from memory.")
		mem.clear()
		intmem -= int('0.00' + str(len(mem)/10))
	elif command == 'clear':
		os.system('clear')
	elif command == 'again':
		run.run(history[len(history) - 1][0], intmem)
	elif command[0:4] == 'run ':
		run.run(open(command[4:len(command)], 'r').readline(), intmem)
	elif command == 'id':
		print(ID)
	elif command == 'return':
		pass
	elif command[0:6] == 'sleep ':
		time.sleep(int(command[6:len(command)]))
	elif command == 'df':
		print('Disk Space')
		print('---------------------------------------------')
		a = os.listdir('.')
		a.remove('.upm')
		a.remove('main.py')
		a.remove('__pycache__')
		a.remove('pyproject.toml')
		a.remove('poetry.lock')
		rawsize = 0
		for item in a:
			try:
				filetype = item[item.index('.') + 1:len(item)].upper() + ' File'
			except ValueError:
				filetype = 'Directory'
			size = os.path.getsize(f'{item}')
			rawsize += os.path.getsize(f'{item}')
			if size in range(0, 1000):
				size = str(size) + ' bytes'
			elif size in range(1000, 1000000):
				size = str(round(size/1000, 3)) + ' KB'
			elif size in range(1000000, 10000000):
				size = str(round(size/1000000, 3)) + ' MB'
			elif size in range(1000000000, 10000000000000):
				size = str(round(size/1000000000, 3)) + ' GB'
			print(f'|{item} ' + ' '*(20 - len(item)) + f'|{size}' + ' '*(10 - len(str(size))) + '|' + ' '*(10 - len(filetype)) + f'{filetype}|')
		print('---------------------------------------------\n')
		size = rawsize
		if size in range(0, 1000):
			size = str(size) + ' bytes'
		elif size in range(1000, 1000000):
			size = str(round(size/1000, 3)) + ' KB'
		elif size in range(1000000, 10000000):
			size = str(round(size/1000000, 3)) + ' MB'
		elif size in range(1000000000, 10000000000000):
			size = str(round(size/1000000000, 3)) + ' GB'
		print(f'Memory Used: {size}')
		size = 5000000000 - rawsize 
		if size in range(0, 1000):
			size = str(round(size)) + ' bytes'
		elif size in range(1000, 1000000):
			size = str(round(size/1000, 3)) + ' KB'
		elif size in range(1000000, 10000000):
			size = str(round(size/1000000, 3)) + ' MB'
		elif size in range(1000000000, 10000000000000):
			size = str(round(size/1000000000, 3)) + ' GB'
		print(f'Free disk space: {size}')
	if len(mem) == 300:
		print(red, "Memory has reached it's limit. ")
	elif command == 'clear':
		os.system('clear')
	elif command == 'exit':
		exec(compile(open('main.py', 'r').read(), 'code.py', 'exec'))
	elif command == 'reboot':
		os.system('clear')
		mem.clear()
		import os, zipfile, datetime, run, random
		ID = hex(random.randint(0, 2**16))
		intmem = 0.000
		mem = []
		direct = str()
		filename = None
		dopen = False
		red = '\b\033[31m\033[1m'
		green = '\b\033[32m\033[1m'
		yellow = '\b\033[33m\033[1m'
		history = list()
	elif command == '':
		pass
	else:
		print(red, f"{command} is not regonized as a shell command.")