def linearSearchProduct(productlist, targetproduct):
  indices = []
  for index, product in enumerate(productlist):
    if product == targetproduct:
      indices.append(index)

  return indices


products = ["suba", "krishna", "suba", "krishna", "suba", "krishna"]
target = "krishna"
result = linearSearchProduct(products, target)
print(result)