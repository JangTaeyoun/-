class TreeNode:
    def __init__(self, key):
        self.left = None    # 왼쪽 자식 노드
        self.right = None   # 오른쪽 자식 노드
        self.val = key      # 노드의 값 (알파벳)

def is_complete_binary_tree(root):
    if not root:
        return True

    queue = [root]
    leaf_started = False  # 마지막 레벨에서 노드가 시작되었는지 여부

    while queue:
        current = queue.pop(0)

        if not current:
            leaf_started = True  # 노드가 비어있으면 마지막 레벨 시작
        elif leaf_started:
            return False  # 마지막 레벨 이후에 노드가 추가되면 완전 이진 트리 아님
        else:
            queue.append(current.left)
            queue.append(current.right)

    return True

# 알파벳으로 이루어진 완전 이진 트리
#         A
#        / \
#       B   E
#      / \   \
#     C   D   F
alphabet_tree = TreeNode('A')
alphabet_tree.left = TreeNode('B')
alphabet_tree.right = TreeNode('E')
alphabet_tree.left.left = TreeNode('C')
alphabet_tree.left.right = TreeNode('D')
alphabet_tree.right.right = TreeNode('F')

# 완전 이진 트리인지 확인하고 결과 출력
print(is_complete_binary_tree(alphabet_tree))  # 출력: False
