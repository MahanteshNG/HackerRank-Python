def count_substring(string, sub_string):
    count=0
    count=sum(count+1  for i in range(0,len(string)) if string[i:i+(len(sub_string))]==sub_string)
    return count

