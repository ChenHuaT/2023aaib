s = "abcdabcd"
d = {}
for c in s:
  if c in d:
    d[c] = d[c] + 1
  else:
    d[c] = 1
  print('�{�b�ݨ쪺�r���O', c, '�r��O', d)