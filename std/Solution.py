def solve(case_num):
    input_args_list = parse_input()
    # find solution from input args
    raise NotImplemented
    # if not validate_solution(solutions):
    #     raise Exception
    # output(case_num, solutions)


def validate_solution(*args):
    raise NotImplemented


def parse_input():
    """
    Uses input() to parse input from file
    :return: (tuple) input arguments for test case
    """
    input_args_list = tuple(input().split())
    # manipulate input arguments
    return input_args_list


def output(case_num, *args):
    """
    generic method that outputs results in args
    """
    print(OUTPUT_TEMPLATE.format(
        case_num=case_num,
        args=args
    ))


OUTPUT_TEMPLATE = "Case #{case_num}: {args}"

if __name__ == "__main__":
    NUMBER_OF_TEST = int(input())
    for CASE_NUMBER in range(1, NUMBER_OF_TEST + 1):
        solve(CASE_NUMBER)
