items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(),
        key=lambda item: item[1]["calories"] / item[1]["cost"],
        reverse=True,
    )

    selected_items, total_cost, total_calories = [], 0, 0
    for item_name, details in sorted_items:
        if (new_cost := total_cost + details["cost"]) <= budget:
            selected_items.append(item_name)
            total_cost, total_calories = (
                new_cost,
                total_calories + details["calories"],
            )

    return {"products": selected_items, "cost": total_cost, "calories": total_calories}


def dynamic_programming(items, budget):
    item_names = list(items.keys())

    dp_table = [[0 for x in range(budget + 1)] for y in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        item_name = item_names[i - 1]
        item_cost = items[item_name]['cost']
        item_calories = items[item_name]['calories']

        for v in range(1, budget + 1):
            if item_cost <= v:
                dp_table[i][v] = max(
                    item_calories + dp_table[i - 1][v - item_cost], dp_table[i - 1][v])
            else:
                dp_table[i][v] = dp_table[i - 1][v]

    selected_items = []
    temp_budget = budget

    for i in range(len(items), 0, -1):
        item_name = item_names[i - 1]
        item_cost = items[item_name]['cost']

        if dp_table[i][temp_budget] != dp_table[i - 1][temp_budget]:
            selected_items.append(item_name)
            temp_budget -= item_cost

    return {"products": selected_items, "cost": budget - temp_budget, "calories": dp_table[len(items)][budget]}

budget = 100
# budget = 40

print("Greedy_algorithm:")
print(greedy_algorithm(items, budget))
print("Algorithm_of_dynamic_programming:")
print(dynamic_programming(items, budget))

