"""
* 스택(stack)이란 쌓아 올린다는 것을 의미한다.
* 따라서 스택 자료구조라는 것은 책을 쌓는 것처럼 차곡차곡 쌓아 올린 형태의 자료구조를 말한다.

* [Node Class]
* - item
* - pointer : 다음 node를 가리키므로 다음 node를 저장하고 아무것도 가리키지 않으면 None을 저장한다.

* [LinkedList]
* - head : 가장 첫 번째 node, node가 없으면 None을 저장한다.
* - length : int 타입, 현재 노드(데이터)의 개수를 의미한다.

* [Stack] : LinkedList를 상속받는다.
* - push(item) : Stack 자료구조에 item을 받아 노드로 만든 다음 밀어넣는다.
* - pop() : Stack 자료구조에서 마지막 node를 제거하고 해당 Item을 반환한다.
"""
from typing import List, Tuple, Dict, Optional
class Node:

    def __init__(self, item, pointer : Optional["Node"]):
        self.item = item
        self.pointer = pointer


class LinkedList:

    head : Node = None
    stack : List["node"] = []
    def __init__(self, node : Node):
        if LinkedList.stack.length == 0 :
            LinkedList.head = node

class Stack(LinkedList):

    def __init__(self, item):
        super().__init__()
        self.item = item
    def push(self):
        LinkedList.stack.push(self.item)

    def pop(self):
        if LinkedList.stack.length == 0 :
            raise ValueError("스택에 데이터 존재하지 않습니다.")
        else:
            return LinkedList.stack.pop()


stack = Stack()

stack.push(12)