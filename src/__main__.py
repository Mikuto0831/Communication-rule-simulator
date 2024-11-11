from random import randint

from modules.nodes.node import Node
from modules.posts.post import Post

NODE_NUM = 10
POST_NUM = 1
SIMULATE_NUM = 1000
MAX_IGNITION_NUM = 100

def test(max_ignition_num:int = 10):
    full = False

    # nodeの作成
    nodes = [Node() for _ in range(NODE_NUM)]

    # ポスト作成とノード間同期 (ポスト数: POST_NUM, 合計明示的同期回数: )
    while (post_num := Post.get_count_all()) < POST_NUM:
            Node.create_post_by_random_node(f"title: {post_num}", f"content: {post_num} content")

    for _ in range(max_ignition_num):
        nodes[randint(0, NODE_NUM - 1)].sync_node_posts()
        if all([node.count_posts() == POST_NUM for node in nodes]):
            # 全てのノードがPOST_NUMのポストを持っている場合
            break
    else:
        full = True

    # ノードごとのポスト数表示
    # print("Result:")
    # for node in nodes:
    #     print(f"Node {node.get_id()}: {node.count_posts()}")
    #     # print(node.show_posts())
    #     print("--------------------")

    return full

if __name__ == '__main__':
    count = 0
    sum = 0.0
    min_sync_cnt = 999999
    max_sync_cnt = 0
    try:
        for i in range(SIMULATE_NUM):
            Node.reset_sync_count()
            ignition_full = test(MAX_IGNITION_NUM)
            sync_cnt = Node.get_sync_count()
            if ignition_full:
                continue
            count += 1
            sum += sync_cnt
            if max_sync_cnt < sync_cnt:
                max_sync_cnt = sync_cnt
            if min_sync_cnt > sync_cnt:
                min_sync_cnt = sync_cnt
    finally:
        print()
        print(f"合計シミュレート回数:{SIMULATE_NUM}")
        print("以下の結果は、全てのノードがPOST_NUMのポストを持っていない場合はカウントされません")
        print(f"発火の規定回数:{MAX_IGNITION_NUM}")
        print(f"規定回数の発火以内に浸透した回数:{count}")
        print(f"平均通信回数:{sum/count}")
        print(f"最大通信回数:{max_sync_cnt}")
        print(f"最小通信回数:{min_sync_cnt}")
