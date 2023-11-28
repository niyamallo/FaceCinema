import requests

url = "https://api.themoviedb.org/3/genre/movie/list?language=ko"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0Mjg2OTk2YWY2OTQ3MTFkZGIwMGFiN2U5ZmNkZTZlNyIsInN1YiI6IjYzZDMxYjcwNWEwN2Y1MDA5ZTk4MDRkOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.c5m_oT5VQDwh4FD3hVWIgC3K0DQrn0eZgQiYt2os3ww"
}

response = requests.get(url, headers=headers)

print(response.text)