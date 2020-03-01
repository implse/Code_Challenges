# Given a list of packages that need to be built and the dependencies
# for each package determine a valid order in which to build packages.

# O :
# 1 : 0
# 2 : 0
# 3 : 2, 1
# 4 : 4

#output : 0, 1, 2, 3, 4


def package_dependencies(dependencies):
  result = list()
  visiting = set([])
  visited = set([])

  def dfs(node):
    if node in visited:
      return
    visiting.add(node)
    for neighbor in dependencies[node]:
      if neighbor in visiting:
        raise Exception("Detect cycle in dependency Graph")
      if neighbor not in visited:
        dfs(neighbor)
    visiting.remove(node)
    visited.add(node)
    result.append(node)

  for node in dependencies.keys():
    dfs(node)
  return result


# Test
dependencies = {0: [], 1: [0], 2: [0], 3: [1, 2], 4: [3]}

print(package_dependencies(dependencies))
