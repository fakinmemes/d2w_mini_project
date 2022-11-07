
def merge(array, x, p, q, r):
  left_array = array[p: q +1]
  right_array = array[ q +1: r +1]
  len_left = q - p + 1
  len_right = r - q
  left_hold = 0
  right_hold = 0
  dest = p

  # When both sides can progress
  while left_hold < len_left and right_hold < len_right:
    # do a comparison
    if x(left_array[left_hold]) <= x(right_array[right_hold]):
      array[dest] = left_array[left_hold]
      left_hold += 1
    else:
      array[dest] = right_array[right_hold]
      right_hold += 1
    dest += 1
  # When only the left side can progress
  while left_hold < len_left:
    array[dest] = left_array[left_hold]
    left_hold += 1
    dest += 1
  # When only the right side can progress
  while right_hold < len_right:
    array[dest] = right_array[right_hold]
    right_hold += 1
    dest += 1
  pass

def mergesort_recursive(array, x, p, r):
  if p < r:
    # find midpoint to split
    q = (p + r) // 2
    # merge sort left side
    mergesort_recursive(array, x, p, q)
    # merge sort right side
    mergesort_recursive(array, x, q + 1, r)
    # merge both sides and sort
    merge(array, x, p, q, r)
  pass


def mergesort(array, byfunc=None):
  x = byfunc
  mergesort_recursive(array, x, 0, len(array ) -1)
  pass


class Stack:
  def __init__(self):
    self.__items = []

  def push(self, item):
    self.__items.append(item)
    pass

  def pop(self):
    if len(self.__items) == 0:
      return None
    else:
      hold = self.__items[len(self.__items) - 1]
      del self.__items[len(self.__items) - 1]
      return hold
    pass

  def peek(self):
    if len(self.__items) == 0:
      return None
    else:
      return self.__items[len(self.__items) - 1]
    pass

  @property
  def is_empty(self):
    if len(self.__items) == 0:
      return True
    else:
      return False
    pass

  @property
  def size(self):
    return len(self.__items)
    pass

class EvaluateExpression:
  # copy the other definitions
  # from the previous parts
    valid_char = '0123456789+-*/() '
    operator = '+-*/()'
    def __init__(self, string=""):
        self._expression = string
        pass

    @property
    def expression(self):
        return self._expression
        pass

    @expression.setter
    def expression(self, new_expr):
        hold_expr = ""
        for x in range(len(new_expr)):
            if new_expr[x] in self.valid_char:
                hold_expr += new_expr[x]
            else:
                hold_expr = ""
                break
        self._expression = hold_expr
        pass

    def insert_space(self):
        hold_str = ""
        for x in range(len(self._expression)):
            if self._expression[x] in self.operator:
                hold_str += " "
                hold_str += self._expression[x]
                hold_str += " "
            else:
                hold_str += self._expression[x]
        self._expression = hold_str
        return self._expression
        pass

    def process_operator(self, operand_stack, operator_stack):
        right = operand_stack.pop()
        left = operand_stack.pop()
        item = operator_stack.pop()
        if item == "+":
            operand_stack.push(left + right)
        elif item == "-":
            operand_stack.push(left - right)
        elif item == "*":
            operand_stack.push(left * right)
        elif item == "/":
            operand_stack.push(left // right)
        pass

    def evaluate(self):
        operand_stack = Stack()
        operator_stack = Stack()
        expression = self.insert_space()
        tokens = expression.split()
        for elem in tokens:
            if elem not in self.operator:
                operand_stack.push(int(elem))
            elif elem =="+" or elem == "-":
                while operator_stack.peek() not in [None,"(", ")"]:
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.push(elem)
            elif elem =="*" or elem =="/":
                while operator_stack.peek() in ["*","/"]:
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.push(elem)
            elif elem == "(":
                operator_stack.push(elem)
            elif elem == ")":
                while operator_stack.peek()!="(":
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.pop()
        while operator_stack.peek() is not None:
            self.process_operator(operand_stack, operator_stack)
        return operand_stack.peek()


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





