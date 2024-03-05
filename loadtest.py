from locust import HttpUser, task, between

class LoadUser(HttpUser):
    wait_time = between(5, 15)  # 각 사용자 간 대기 시간 (초)

    @task(3)
    def basic_connecting(self):
        request_data = {
            'email' : 'test@test.com'
        }
        response = self.client.post("/verify/email_check" ,json = request_data) 
        if response.status_code == 200:
            pass
        else:
            pass
