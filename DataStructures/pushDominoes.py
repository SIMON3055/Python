'''
There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left, dominoes[i] = 'R', if the ith domino has been pushed to the right, and dominoes[i] = '.', if the ith domino has not been pushed. Return a string representing the final state.

Example 1:

Input: dominoes = "RR.L" Output: "RR.L" Explanation: The first domino expends no additional force on the second domino. Example 2:

Input: dominoes = ".L.R...LR..L.." Output: "LL.RR.LLRRLL.."
'''
import  collections
def pushDominoes(dominoes: str) -> str:
    dominoes_list = list(dominoes)
    # * Start the BFS traversal.
    # * Push all the `L` and `R` into the queue for processing.
    queue = collections.deque(
        [(idx, d) for idx, d in enumerate(dominoes_list) if d != "."]
    )

    while queue:
        cur_idx, cur_dominoe = queue.popleft()
        if cur_dominoe == "L" and cur_idx > 0 and dominoes_list[cur_idx - 1] == ".":
            queue.append((cur_idx - 1, "L"))
            dominoes_list[cur_idx - 1] = "L"

        elif (
                cur_dominoe == "R"
                and cur_idx + 1 < len(dominoes_list)
                and dominoes_list[cur_idx + 1] == "."
        ):
            if (
                    cur_idx + 2 < len(dominoes_list)
                    and dominoes_list[cur_idx + 2] == "L"
            ):
                queue.popleft()

            else:
                queue.append((cur_idx + 1, "R"))
                dominoes_list[cur_idx + 1] = "R"

    return "".join(dominoes_list)


if __name__ == "__main__":
    print(pushDominoes("RR.L"))
    print(pushDominoes(".L.R...LR..L.."))