1. Valid Anargam
Two strings are anargam if they are made of the same characters with the same frequency.

s1 = 'garden'
s2 = 'danger'

def is_anargam(s1,s2):
  if len(s1) != len(s2) :
    return false
  freq1 = {}
  fre12 = {}
  for ch in s1:
    if ch in freq1:
      freq1[ch] += 1
    else :
      freq1[ch] = 1
  for ch in s2
