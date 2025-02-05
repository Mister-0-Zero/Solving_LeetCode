class Solution:
    def canJump(self, nums: list[int]) -> bool:
        self.i = 0
        self.kol_zero = 0
        self.max_jump = max(nums)
        self.nums = nums

        #основа алгоритма, перемещаемся на максимальный прыжок, если попадаем в 0, то считаем количество нулей
        #и затем проверяем, можем ли мы их перепрыгнуть
        while self.i < len(self.nums):
            if self.nums[self.i] != 0:
                if self.kol_zero != 0:
                    #собственно проверка
                    if not self.check():
                        return False
                else:
                    self.i += self.nums[self.i]
            else:
                self.kol_zero += 1
                self.i += 1

        #рассматриваем случай если в конце были нули, если он только один, то мы могли войти в него
        #например: [..., 1, 1, 0]
        if self.kol_zero > 1:
            #уменьшаем на единицу, так как теперь задача не перепрыгнуть нули, а либо перепрыгнуть или войти в последний ноль
            self.i -= 1
            self.kol_zero -= 1
            if not self.check():
                return False
        return True

    def check(self):
        if self.kol_zero > self.max_jump:
            return False
        current_ind = self.i - self.kol_zero - 1
        flag = 1
        while self.i - current_ind <= self.max_jump and current_ind > 0:
            if self.nums[current_ind] >= self.i - current_ind:
                self.i = current_ind + self.nums[current_ind]
                flag = 0
                self.kol_zero = 0
                break
            else:
                current_ind -= 1
        if flag:
            return False
        return True



instance = Solution()
res = instance.canJump([5,9,3,2,1,0,2,3,3,1,0,0,0])
print(res)