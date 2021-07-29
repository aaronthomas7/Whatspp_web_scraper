f = open('output_whatsapp_web.txt','r')

data = f.read()
words = data.split()
print(words)
result = {}
for word in words:
	if word not in result:
		result[word]=0
	result[word]+=1
print(result)