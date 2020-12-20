def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    op_counter = 0
    cl_counter = 0
    op_list = []
    if brackets_row == '':
        return True
    for i in brackets_row:
        if i == '(':
            op_counter += 1
            op_list.append(i)
        elif i == ')':
            cl_counter += 1
            if len(op_list)>0:
                op_list.pop()
            else:
                return False
    if op_counter != cl_counter:
        return False
    else:
        return True


if __name__ == '__main__':
    print(check_brackets("(((()))"))
