

class Payload:
    body = {}
    headers = {}

    def __init__(self, body=None, headers=None):
        self.body = body
        self.headers = headers


posts_post_payload = Payload(
    {
        "title": "foo",
        "body": "bar",
        "userId": 2
    },
    {
        "Content-type": "application/json; charset=UTF-8"
    }
)

posts_put_payload = Payload(
    {
        "id": 1,
        "title": "foo",
        "body": "bar",
        "userId": 2
    },
    {
        "Content-type': 'application/json; charset=UTF-8"
    }
)

posts_patch_payload = Payload(
    {
        "title": "foo"
    },
    {
        "Content-type': 'application/json; charset=UTF-8"
    }
)