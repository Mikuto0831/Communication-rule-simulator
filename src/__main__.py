from random import randint

from modules.nodes.node import Node
from modules.posts.post import Post

NODE_NUM = 10
POST_NUM = 1

def main(ignition_num:int = 10):
    # nodeの作成
    nodes = [Node() for _ in range(NODE_NUM)]

    # ポスト作成とノード間同期 (ポスト数: POST_NUM, 合計明示的同期回数: )
    for _ in range(ignition_num):
        while (post_num := Post.get_count_all()) < POST_NUM:
            Node.create_post_by_random_node(f"title: {post_num}", f"content: {post_num} content")
        nodes[randint(0, NODE_NUM - 1)].sync_node_posts()

    # ノードごとのポスト数表示
    # print("Result:")
    # for node in nodes:
    #     print(f"Node {node.get_id()}: {node.count_posts()}")
    #     # print(node.show_posts())
    #     print("--------------------")
    count = 0
    for node in nodes:
        count += node.count_posts()

    return count/POST_NUM/NODE_NUM

if __name__ == '__main__':
    count = 0
    sum = 0.0
    result = 0.0
    try:
        while result < 1.0:
            Node.reset_sync_count()
            result = main()
            # print(f"{count+1}:{result}")
            sum += result
            if count >= 5000:
                break
            count += 1
    finally:
        print()
        print(f"count:{count}")
        print(f"average:{sum/count}")
        print(f"sync_count:{Node.sync_count}")
