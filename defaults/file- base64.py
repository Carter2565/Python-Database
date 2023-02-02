import base64

with open(input('What is the file name/location?: '), "rb") as f:
  file = f.read()
  image = base64.b64encode(file).decode()
  # print(f"\n {image}")

f = open(input('Enter full name for file. Ex: pfp.base64.: '), "a")
f.write(image)
f.close()