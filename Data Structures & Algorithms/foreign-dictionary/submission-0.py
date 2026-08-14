class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        def compare(w1, w2):
            for a, b in zip(w1, w2):
                if a != b:
                    return a, b
            return "", ""

        adj_list = defaultdict(list)
        chars = {c for w in words for c in w}

        for i in range(1, len(words)):

            c1, c2 = compare(words[i-1], words[i])
            if c1 != "":
                adj_list[c1].append(c2)
            elif len(words[i-1]) > len(words[i]):
                return ""

        state = {}

        def dfs(cur):

            if cur in state:
                return state[cur]

            state[cur] = False
            for nei in adj_list[cur]:
                if not dfs(nei):
                    return False
            state[cur] = True

            order.append(cur)
            return True

        order = []
        for c in chars:
            if not dfs(c):
                return ""

        return "".join(reversed(order))