class solution:
  def conRevstr(self, s1: str, s2: str) -> string:
    # code here
    result = s1 + s2
    ans = ""

    for i range(len(result) -1, -1, -1):
         ans += result[i]

     return ans
