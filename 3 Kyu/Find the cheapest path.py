import heapq #priority queue (min-heap)

def cheapest_path(t, start, finish):
    rows, cols = len(t), len(t[0])
    costs = {start: t[start[0]][start[1]]} # minimum known cost to reach each node
    parent = {start: None} #Keep the previous node for each node

    pq = [(t[start[0]][start[1]], start)] # a list containing one tuple (cost, node)
    heapq.heapify(pq) #turn the list into a valide min-heap

    directions = {(0, 1): "right", 
                  (0, -1): "left", 
                  (1, 0): "down", 
                  (-1, 0): "up"}

    #The start of Dijkstra's algorithm
    while pq:
        curr_cost, (r, c) = heapq.heappop(pq) # pop the lowest cost from the priority queue

        # check the current node to the finish node
        if (r, c) == finish:
            path = []
            node = finish
            while parent[node] is not None:
                prev = parent[node]
                dr, dc = node[0] - prev[0], node[1] - prev[1]
                path.append(directions[(dr, dc)])
                node = prev
            path.reverse()
            return path
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_cost = curr_cost + t[nr][nc]
                if (nr, nc) not in costs or new_cost < costs[(nr, nc)]:
                    costs[(nr, nc)] = new_cost
                    parent[(nr, nc)] = (r, c)
                    heapq.heappush(pq, (new_cost, (nr, nc)))
    return None

t = [[1,9,1],
     [2,9,1],
     [2,1,1]]

start = (0, 0)
finish = (0, 2)

cheapest_path(t, start, finish)
