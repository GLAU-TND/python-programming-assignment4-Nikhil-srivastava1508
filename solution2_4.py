n=eval(input())
def new(dict):
  try:
    for k in dict:
      if type(dict[k])==type({}):
        for i in dict[k]:
          dict[k+i]=dict[k][i]
        dict.pop(k)
        new(dict)
    else:
      print(dict)
  except RuntimeError:
    pass
new(n)
