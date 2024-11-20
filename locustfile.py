from locust import *

class indexTest(HttpUser):
    wait_time = between(0.5, 2.5)

    def on_start(self):
        self.login()
    
    def login(self):
        response = self.client.get('sesion/login/')
        csrftoken = response.cookies['csrftoken']
        self.client.post('/sesion/login/',
                         {'userName': 'emilio', "password":"1234"},
                         headers={'X-CSRFToken':csrftoken})

    @task
    def getIndex(self):
        self.client.get('/noticias/index/')
        self.client.get('noticias/noticias_climaticas/')
        self.client.get('noticias/noticias_ciencia_tecnologia/')
        self.client.get('noticias/noticias_economia/')
        self.client.get('noticias/noticias_internacionales/')
        self.client.get('noticias/noticias_deportes/')
        self.client.get('noticias/noticias_fisica_cuantica/')
        self.client.get('noticias/periodistas/')
        self.client.get('noticias/noticias_policial/')
