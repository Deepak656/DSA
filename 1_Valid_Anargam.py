1. Valid Anargam
Two strings are anargam if they are made of the same characters with the same frequency.

s1 = 'garden'
s2 = 'danger'

def is_anargam(s1,s2):
  if len(s1) != len(s2) :
    return false
  freq1 = {}
  freq2 = {}
  for ch in s1:
    if ch in freq1:
      freq1[ch] += 1
    else :
      freq1[ch] = 1
  for ch in s2:
    if ch in freq2:
      freq2[ch] +=1
    else :
      freq2[ch] =1
for key in freq1 :
  if key not in freq2 or freq1[key] != freq2[key] :
    return false
return true
    
