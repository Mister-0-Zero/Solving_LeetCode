class Solution:
    def simplifyPath(self, path: str) -> str:
        list_path = path.split("/")
        ind = 0
        path_res = []

        while ind < len(list_path):
            if list_path[ind] != "." and list_path[ind] != '':
                if list_path[ind] == "..":
                    path_res = path_res[:-1]
                else:
                    path_res.append(list_path[ind])
            ind += 1

        path_res = "/" + '/'.join(path_res)

        return path_res

instance = Solution()
path = "/a/../sdfsdf/sdf/sdff/././../1231.///sdf/.///sdf//123/"
print(f"Original the path: {path}")
res = instance.simplifyPath(path)
print("\n", f"Processed string: {res}")
