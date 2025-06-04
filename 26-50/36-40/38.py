class Solution:
    def countAndSay(self, n: int) -> str:

        def f(n, count = 1, string = '1'):

            if count == n:
                return string

            string_ = ''
            ind = 0

            while ind != len(string):
                sim = string[ind]
                sim_countSim = {sim: 0}

                while ind != len(string) and sim == string[ind]:
                    sim_countSim[sim] += 1
                    ind += 1
                string_ += f'{sim_countSim[sim]}{sim}'

            return f(n, count + 1, string_)

        return f(n)

instance = Solution()
res = instance.countAndSay(8)
print(res)

class Solution:
    def countAndSay(self, n: int) -> str:

        def f(n, count = 1, string = '1'):

            if count == n:
                return string

            string_ = ''
            ind = 0
            sim_countSim = []

            while ind != len(string):
                sim = string[ind]
                count_int = 1
                ind += 1

                while ind != len(string) and sim == string[ind]:
                    count_int += 1
                    ind += 1
                sim_countSim.append([sim, count_int])

            return f(n, count + 1, ''.join([f'{value}{key}' for key, value in sim_countSim]))

        return f(n)

instance = Solution()
res = instance.countAndSay(8)
print(res)