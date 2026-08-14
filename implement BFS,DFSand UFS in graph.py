print("Hello, I'll take you to the GOAL")
mapRooms = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': ['E']
}

startRoom = 'A'
goalRoom = 'F'

print("Starting Room:", startRoom)
print("Goal Room:", goalRoom)
print("Map of rooms:" ,mapRooms)
print(r"            A          ")
print(r"           / \         ")
print(r"          B   C        ")
print(r"         / \   \       ")
print(r"        D   E   F      ")

def bfs(start, goal):
  queue = [start]
  visited =[]
  order =[]
  while queue:
    current = queue.pop(0)
    if current in visited:
      continue
    visited.append(current)
    order.append(current)

    if current == goal:
      return order

    for neighbor in mapRooms[current]:
      queue.append(neighbor)

  return order

order = bfs("A","F")
print(order)
print(len(order))

def dfs(start, goal):
  stack = [start]
  visited =[]
  order =[]
  while stack:
    current = stack.pop()
    visited.append(current)
    order.append(current)
    if current == goal:
      return order

    for neighbor in mapRooms[current]:
      stack.append(neighbor)

  return order

order = dfs("A","F")
print(order)
print(len(order))

def find_all_paths(start, goal, graph):
    all_paths = []

    def dfs_recursive(current_node, current_path):
        # Add current_node to the current path
        current_path = current_path + [current_node]

        # If the current_node is the goal, we found a path
        if current_node == goal:
            all_paths.append(current_path)
            return

        # Explore neighbors
        for neighbor in graph.get(current_node, []):
            # Avoid cycles within the current path
            if neighbor not in current_path:
                dfs_recursive(neighbor, current_path)

    dfs_recursive(start, [])
    return all_paths

print("\nAll Paths from", startRoom, "to", goalRoom, ":")
all_paths = find_all_paths(startRoom, goalRoom, mapRooms)

if all_paths:
    for i, path in enumerate(all_paths):
        print(f"Path {i+1}: {path} (Length: {len(path)})")
else:
    print("No paths found.")
