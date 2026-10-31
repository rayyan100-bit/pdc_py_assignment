shopping_list = ["apples", "bread", "coffee"]

shopping_list.append("yogurt")
shopping_list.extend(["carrots", "bread"])
shopping_list.insert(1, "bananas")

print("Shopping list:", shopping_list)
print("Bread appears", shopping_list.count("bread"), "times")
print("Carrots are at position", shopping_list.index("carrots"))

removed_item = shopping_list.pop()
print("Removed the last item:", removed_item)

shopping_list.remove("coffee")
shopping_list.sort()

print("Sorted shopping list:", shopping_list)
print("Items remaining:", len(shopping_list))