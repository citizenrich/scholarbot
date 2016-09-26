from locust import HttpLocust, TaskSet


def stuff1(l):
    l.client.get("/v1?date=2016-03&words=putin")


def stuff2(l):
    l.client.get("/v1?date=2016-03&words=neural%20networks")


def stuff3(l):
    l.client.get("/v1?date=2016-03&words=china")


class UserBehavior(TaskSet):
    tasks = {stuff2: 1, stuff3: 1}

    def on_start(self):
        stuff1(self)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 15000  # def 9000


# locust -f ../locust_files/my_locust_file.py --host=http://example.com
