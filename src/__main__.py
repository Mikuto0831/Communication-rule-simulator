from random import randint

from modules.nodes.node import Node
from modules.posts.post import Post

NODE_NUM = 10

def main():
    # nodeの作成
    nodes = [Node() for _ in range(NODE_NUM)]

    # ポスト作成とノード間同期 (ポスト数: 15, 合計明示的同期回数: 100)
    for _ in range(15):
        if (post_num := Post.get_count_all()) < 15:
            Node.create_post_by_random_node(f"title: {post_num}", f"content: {post_num} content")
        nodes[randint(0, NODE_NUM - 1)].sync_node_posts()

    # ノードごとのポスト数表示
    print("Result:")
    for node in nodes:
        print(f"Node {node.get_id()}: {node.count_posts()}")
        # print(node.show_posts())
        print("--------------------")

if __name__ == '__main__':
    main()
