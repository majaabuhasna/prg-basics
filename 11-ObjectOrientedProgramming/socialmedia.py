class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(f'Username: {self.username}')
        index = 1
        for post in self.posts:
            print(f'{index}. {post}')
            index += 1

if __name__ == '__main__':
    user = SocialMediaProfile('johndoe')
    user.add_post("Hello, world!")
    user.add_post("Had a great day at the park!")
    user.add_post("What's up, Natalie? How are you?")

    print('\n--- TIMELINE ---')
    user.display_timeline()