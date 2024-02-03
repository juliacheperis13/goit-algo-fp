def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    selected_items = []
    remaining_budget = budget

    for item_name, item_info in sorted_items:
        if item_info['cost'] <= remaining_budget:
            selected_items.append(item_name)
            remaining_budget -= item_info['cost']

    return selected_items


def dynamic_programming(items, budget):
    num_items = len(items)
    dp_table = [[0] * (budget + 1) for _ in range(num_items + 1)]

    for i in range(1, num_items + 1):
        item_name = list(items.keys())[i - 1]
        cost = items[item_name]['cost']
        calories = items[item_name]['calories']

        for w in range(budget + 1):
            if cost <= w:
                dp_table[i][w] = max(dp_table[i - 1][w],
                                     dp_table[i - 1][w - cost] + calories)
            else:
                dp_table[i][w] = dp_table[i - 1][w]

    selected_items = []
    w = budget
    for i in range(num_items, 0, -1):
        if dp_table[i][w] != dp_table[i - 1][w]:
            item_name = list(items.keys())[i - 1]
            selected_items.append(item_name)
            w -= items[item_name]['cost']

    return selected_items
  
if __name__ == "__main__":
  items = {
      "pizza": {"cost": 50, "calories": 300},
      "hamburger": {"cost": 40, "calories": 250},
      "hot-dog": {"cost": 30, "calories": 200},
      "pepsi": {"cost": 10, "calories": 100},
      "cola": {"cost": 15, "calories": 220},
      "potato": {"cost": 25, "calories": 350}
  }

  budget = 70

  print("Greedy Algorithm:")
  print(greedy_algorithm(items, budget))

  print("\nDynamic Programming:")
  print(dynamic_programming(items, budget))
