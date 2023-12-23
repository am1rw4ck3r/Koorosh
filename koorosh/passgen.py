# Amir Zare / KooRoSH

class Generator(object):
 def __init__(self,name):
  self.name  = self.filter(name)
  self.keys  = []
  self.list  = ''
  self.nums  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
  21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,
  43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,
  65,66,67,68,69,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,
  86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,1400,1399,1398,1397,
  1396,1395,1394,1393,1392,1391,1390,1389,1388,1387,1386,1386,1385,
  1384,1383,1382,1381,1380,1379,1378,1377,1376,1375,1374,1373,1372,
  1371,1370,1369,1368,1367,1366,1365,1364,1363,1362,1361,1360,1359,
  1358,1357,1356,1355,1354,1353,1352,1351,1350,123,1234,12345,123456,
  1234567,12345678,123456789,321,4321,54321,654321,7654321,87654321,
  987654321,1010,1111,2222,3333,4444,5555,6666,7777,8888,9999,'!@#','!','@','#','%','&','_','-']
  self.com   = ['@dmin','page','instagram','insta','password','name','p@ssword','p@ssw0rd','admin','phone']

 def toFile(self):
  with open('password.lst','w+') as file:
   file.write(self.list)

 def filter(self,text):
  return text.replace('\n','')

 def read(self):
  for passwrd in self.keys:
   yield '{}\n'.format(passwrd)

 def generate(self,text,num):
  self.keys.append('{}{}'.format(text.lower(),num))
  self.keys.append('{}{}'.format(text.title(),num))
  #
  self.keys.append('{}.{}'.format(text.lower(),num))
  self.keys.append('{}.{}'.format(text.title(),num))

 def ai(self):
  for num in self.nums:
   self.generate(self.name,num)

  for text in self.com:
   self.keys.append('{}'.format(text))
   for num in self.nums:
    self.generate(text,num)

  for key in self.read():
   self.list=self.list+key
  self.toFile()
