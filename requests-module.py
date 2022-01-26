from cmath import e
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()  # raises an exception if error occurs during downloading
print(type(res))
res.status_code == requests.codes.ok  # returns TRUE
print(len(res.text))
print(res.text[:250])
