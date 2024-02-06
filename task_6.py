def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорійності до вартості в порядку спадання
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    selected_items = {}
    total_cost = 0
    total_calories = 0

    for item, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            selected_items[item] = info
            total_cost += info["cost"]
            total_calories += info["calories"]

    return selected_items, total_cost, total_calories


def dynamic_programming(items, budget):
    # Створюємо таблицю для зберігання оптимальних значень калорійності для кожного бюджету
    dp = [0 for _ in range(budget + 1)]
    item_list = [[] for _ in range(budget + 1)]

    for cost in range(1, budget + 1):
        for item, info in items.items():
            if info["cost"] <= cost:
                # Якщо можемо взяти цю страву і вона покращує загальну калорійність
                if dp[cost - info["cost"]] + info["calories"] > dp[cost]:
                    dp[cost] = dp[cost - info["cost"]] + info["calories"]
                    item_list[cost] = item_list[cost - info["cost"]] + [item]

    # Знайдемо максимальну калорійність і відповідний список страв
    max_calories = dp[budget]
    selected_items = {item: items[item] for item in item_list[budget]}

    return selected_items, budget, max_calories


def print_results(title, selected_items, total_cost, total_calories):
    print(f"{title} Результат:")
    print("Вибрані страви:")
    for item, info in selected_items.items():
        print(
            f"- {item}: вартість {info['cost']}, калорійність {info['calories']}")
    print(f"Загальна вартість: {total_cost}")
    print(f"Загальна калорійність: {total_calories}")
    print("\n")


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

price = 250
print_results("Жадібний алгоритм", *greedy_algorithm(items, price))
print_results("Динамічне програмування", *dynamic_programming(items, price))
