import json
from collections import defaultdict

with open("orders_july_2023.json", "r") as my_file:
    translator = json.load(my_file)

max_price = 0
max_order_price = ''
orders_with_max_price = []

max_quantity = 0
max_order_quantity = ''
orders_with_max_quantity = []

orders_per_day = defaultdict(int)
max_orders_per_day = 0
days_with_max_orders = []

user_order_counts = defaultdict(int)
max_user_orders = 0
users_with_max_orders = []

user_total_spent = defaultdict(float)
max_spent = 0
users_with_max_spent = []

total_order_price = 0
total_order_count = 0
total_items = 0


# цикл по заказам
for order_num, order_info in translator.items():
    price = order_info['price']
    quantity = order_info['quantity']
    date = order_info['date']
    user_id = order_info['user_id']

    # Заказы с самой большой стоимостью
    if price > max_price:
        max_order_price = order_num
        max_price = price
        orders_with_max_price = [order_num]
    elif price == max_price:
        orders_with_max_price.append(order_num)

    # Заказы с самым большим количеством товаров
    if quantity > max_quantity:
        max_quantity = quantity
        orders_with_max_quantity = [order_num]
    elif quantity == max_quantity:
        orders_with_max_quantity.append(order_num)

    # Подсчет заказов по дням
    day = date.split('-')[-2]
    orders_per_day[day] += 1
    current_day_orders = orders_per_day[day]
    if current_day_orders > max_orders_per_day:
        max_orders_per_day = current_day_orders
        days_with_max_orders = [day]
    elif current_day_orders == max_orders_per_day:
        if day not in days_with_max_orders:
            days_with_max_orders.append(day)

    # Подсчет заказов по пользователям
    user_order_counts[user_id] += 1
    current_user_orders = user_order_counts[user_id]
    if current_user_orders > max_user_orders:
        max_user_orders = current_user_orders
        users_with_max_orders = [user_id]
    elif current_user_orders == max_user_orders:
        if user_id not in users_with_max_orders:
            users_with_max_orders.append(user_id)

    # Суммарная стоимость заказов по пользователям
    user_total_spent[user_id] += price
    total_spent = user_total_spent[user_id]
    if total_spent > max_spent:
        max_spent = total_spent
        users_with_max_spent = [user_id]
    elif total_spent == max_spent:
        if user_id not in users_with_max_spent:
            users_with_max_spent.append(user_id)

    # Общие суммы для подсчета средних
    total_order_price += price
    total_order_count += 1
    total_items += quantity

# Средняя стоимость заказа
avg_order_price = total_order_price / total_order_count

# Средняя стоимость товаров в заказе
avg_item_price = total_order_price / total_items

print(f'1. Номера заказов с самой большой стоимостью: {orders_with_max_price}, стоимость заказа: {max_price}')
print(f'2. Номера заказов с самым большим количеством товара: {orders_with_max_quantity}, количество товара: {max_quantity}')
print(f"3. Больше всего заказов {max_orders_per_day} было сделано {days_with_max_orders} числа : ")
print(f"4. Пользователи {users_with_max_orders} сделали наибольшее количество заказов: {max_user_orders}")
print(f"5. Пользователи {users_with_max_spent} набрали наибольшую суммарную стоимость заказов: {max_spent:.2f}")
print(f"6. Средняя стоимость заказа в июле: {avg_order_price:.2f}")
print(f"7. Средняя стоимость товаров в июле: {avg_item_price:.2f}")

