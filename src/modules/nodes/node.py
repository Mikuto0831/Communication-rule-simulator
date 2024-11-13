from random import randint
from uuid import UUID

from modules.posts.post import Post


class Node:
    """
    ノードクラス
    主にここを変更する
    """
    nodes = []
    max_recursions = 4
    sync_count = 0

    def __init__(self) -> None:
        self.__id = len(self.__class__.nodes)
        self.__posts = {}
        self.__class__.nodes.append(self)

    # 基本的なデータ操作
    def get_id(self):
        return self.__id

    def get_posts(self):
        return self.__posts

    def get_posts_data(self):
        return [self.get_post(post_id).get_post_data() for post_id in self.get_post_ids()]

    def get_post(self, post_id: UUID):
        return self.__posts[post_id]

    def get_post_ids(self):
        return self.__posts.keys()

    def create_post(self, title: str, content: str):
        post = Post(title, content)
        self.add_post(post)

    def add_post(self, post):
        self.__posts[post.get_id()] = post

    def add_posts(self, posts):
        self.__posts |= posts

    def remove_post(self, post_id):
        del self.__posts[post_id]

    def sync_node_posts(self):
        self.__class__.post_update_by_random_node(self)

    # デバック用
    def show_posts(self):
        print("Posts:")
        print(self.get_posts_data())

    def count_posts(self):
        return len(self.__posts)

    # ノード間のポスト交換
    @classmethod
    def post_update_by_random_node(cls, node, coll_count: int = 0):
        """
        主なポスト交換アルゴリズムを組む場所(と考えている)

        :param node: ポストを交換するノード
        :param coll_count: 再帰回数
        """
        # 通信回数のカウント(2回(行って戻ってくる)としてカウント)
        cls.sync_count += 2

        if coll_count > cls.max_recursions:
            return
        # 相手ノードの選択
        server_node_id = randint(0, len(cls.nodes) - 1)
        server_node = cls.nodes[server_node_id]

        # ノード間同期
        # REST APIの使用を考えるとPOSTRequestを受け取った側から更新される
        server_node.add_posts(node.get_posts())
        node.add_posts(server_node.get_posts())  # 更新結果に基づき自身を更新

        # POSTされた側がPOST
        cls.post_update_by_random_node(server_node, coll_count + 1)

    # randomなノードでポスト作成
    @classmethod
    def create_post_by_random_node(cls, title: str, content: str):
        node_id = randint(0, len(cls.nodes) - 1)
        node = cls.nodes[node_id]
        node.create_post(title, content)
        # cls.post_update_by_random_node(node)

    @classmethod
    def show_nodes(cls):
        print("nodes:")
        for node in cls.nodes:
            print(node.get_id())

    @classmethod
    def get_sync_count(cls):
        return cls.sync_count

    @classmethod
    def reset_sync_count(cls):
        cls.sync_count = 0

    @classmethod
    def reset_class(cls):
        cls.nodes = []
        cls.reset_sync_count()
        Post.reset_class()