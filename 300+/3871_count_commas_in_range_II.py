
"""
3871. Count Commas in Range II (https://leetcode.com/problems/count-commas-in-range-ii/description/?envType=daily-question&envId=2026-09-09)

  every number from 0 to 999 has no commas
  every number from 1,000 to 999,999 has one comma
  every number from 1,000,000 to 100,000,000 has two commas
  refer to the sets of numbers with equal commas as comma groups

  starting from 1,000 every time you multiply by 1,000 you get a new comma
  might be easier to count upwards from 1 to n

  keep track of the current comma group
  let start and end be the first and last value of the current comma group
    at the start, start = 1000, end = 999,999
      (just return 0 if n < 1000 so you don't have to consider that case)
  
  size of the current comma group = (end-start+1)
  for each commas group, add to total (size of current comma group) * (comma count in a number)

  when current group has been counted, move your start and end pointers to the next group and increment the comma count by 1
    start = end+1, since end was the last number in the previous comma group
    end = (start)*1000-1, (after start = end+1 is performed)

  when end is larger than n, manually count the remainder
  start < n, so the amount of numbers remaining is (n-start+1)
    simply add (n-start+1) * (comma count) to the total and return


  runtime: O(log(n)) solution iterates three digits at a time
  space: O(1)

  solution also works for (https://leetcode.com/problems/count-commas-in-range/submissions/2136838274/?envType=daily-question&envId=2026-09-08)
"""
def countCommas(n: int) -> int:
  if n < 1000:
    return 0

  start = 1000 # beginning of first comma group
  end = (start)*1000-1 #  last number before the next comma group
  commas = 1 # number of commas in a number of the current comma group
  res = 0

  while end < n:
    print(f"start: {start}, end: {end}")
    res += commas * (end-start+1)
    start = end+1
    end = (start)*1000-1
    commas += 1

  res += (n-start+1)*commas
  return res


n = 1002
print(countCommas(n))


  



