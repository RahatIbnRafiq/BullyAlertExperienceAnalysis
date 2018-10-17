
import requests
response = requests.get("https://www.instagram.com/gavinb0603/")
print (response.status_code)
content = str(response.content)
index = content.index("window._sharedData")
content = content[index:]
index = content.index(";</script>")
content = content[:index]
index = content.index("{")
content = content[index:]
print(content)