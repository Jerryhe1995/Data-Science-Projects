def model_error(target,predict):
  target = list(target)
  predict = list(predict)
  if len(target) != len(predict):
      raise ValueError
  error = 0
  for t,p in zip(target,predict):
      if t != p:
          error += 1
  return error/len(target)
