def Solution(gas, cost):
  index = 0
  for index in range(len(gas)):
    total_gas = gas[index] - cost[index]
    if index == len(gas) - 1:
      traverse = 0
    else:
      traverse = index + 1
    while traverse != index:
      if total_gas < 0:
        break
      elif traverse < len(gas) - 1:
        total_gas += (gas[traverse] - cost[traverse])
        traverse += 1
      else:
        print (gas[traverse])
        total_gas += (gas[traverse] - cost[traverse])
        traverse -= 0
    if traverse == index and total_gas >= 0:
      return index
  return -1

# OR

def Solution(gas, cost):
      if sum([(gas[i] - cost[i]) for i in xrange(len(gas))]) < 0:
            return -1

        for j in xrange(len(gas)):
            gas_left = gas[j] - cost[j]
            next_station = (j + 1) % len(gas)
            while gas_left >= 0:
                gas_left = gas_left + (gas[next_station] - cost[next_station])
                next_station = (next_station + 1) % len(gas)
                if next_station == j:
                    return j
        return -1

# OR

def canCompleteCircuit(self, gas, cost):
        cumm_gas, cum_cost = 0,0
        tank,start = 0,0
        for i in range(len(gas)):
            cumm_gas += gas[i]
            cum_cost += cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i+1
        if cumm_gas < cum_cost:
            return -1
        return start
