def getEnvVariable(variable):
	import json
	json.load(open('env.json','r'))[variable]