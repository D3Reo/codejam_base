from functools import partial


def solve(_):
    answers = ...

    raise NotImplemented

    # answer_msg = " ".join([str(answer) for answer in answers])
    # send_to_judge(answer_msg)


def parse_input():
    """
    Uses input() to parse input from file
    :return: (tuple) input arguments for test case
    """
    worker_num, broken_num, attempts_num = (int(arg) for arg in input().split())
    # manipulate input arguments
    return worker_num, broken_num, attempts_num


def send_to_judge(msg):
    print_to_judge(msg)
    comment = input()
    if comment == "-1":
        raise JudgeError
    return comment


print_to_judge = partial(print, flush=True)


class JudgeError(Exception):
    pass


if __name__ == "__main__":
    NUMBER_OF_TESTS, *OTHER_STUFF = [int(arg) for arg in input().split()]
    for _ in range(1, NUMBER_OF_TESTS + 1):
        solve(OTHER_STUFF)
