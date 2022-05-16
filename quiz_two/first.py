import requests as req


def get_emails(username):
    users_json = req.get(r"https://jsonplaceholder.typicode.com/users").json()
    id_posts = []
    id_username = -1
    emails = []
    for user in users_json:
        if user["username"] == username:
            id_username = user["id"]
            break
    if id_username == -1:
        return "Такого юзера нет"
    posts_json = req.get(r"https://jsonplaceholder.typicode.com/posts").json()
    for post in posts_json:
        if post["userId"] == id_username:
            id_posts.append(post["id"])
    comments_json = req.get(r"https://jsonplaceholder.typicode.com/comments").json()
    for comment in comments_json:
        if comment["postId"] in id_posts:
            emails.append(comment["email"])
    return emails


if __name__ == "__main__":
    print(get_emails("Bret"))
