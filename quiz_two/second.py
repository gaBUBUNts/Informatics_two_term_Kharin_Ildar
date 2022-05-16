topics = []
users = {}


def create_topic(topic_name: str):
    topics.append(topic_name)


def subscribe(user_id: int, topic: str):
    if user_id not in users.keys():
        users[user_id] = []
    users[user_id].append(topic)


def post_fedd(topic: str, feed_id: int):
    for key, value in users:
        if value == topic:
            print(f"пользователь {key} получил новость {feed_id}")
