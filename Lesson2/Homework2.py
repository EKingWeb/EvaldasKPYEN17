packages_sent = 0
total_weight = 0
current_pkg_weight = 0
items_processed = 0

max_unused = -1
max_unused_pkg_num = 0

print("Enter the maximum number of items to be shipped:")
max_items = int(input())

while items_processed < max_items:
    print("Enter item weight (1-10 kg, or 0 to terminate):")
    weight_input = input()

    if weight_input == "0":
        break

    if weight_input == "1" or weight_input == "2" or weight_input == "3" or weight_input == "4" or weight_input == "5" or weight_input == "6" or weight_input == "7" or weight_input == "8" or weight_input == "9" or weight_input == "10":
        item_weight = int(weight_input)
    else:
        print("Error: Invalid input. Please enter a valid number between 1 and 10.")
        continue

    items_processed += 1

    if current_pkg_weight + item_weight > 20:
        packages_sent += 1
        pkg_unused = 20 - current_pkg_weight
        total_weight += current_pkg_weight

        if pkg_unused > max_unused:
            max_unused = pkg_unused
            max_unused_pkg_num = packages_sent

        current_pkg_weight = item_weight
    else:
        current_pkg_weight += item_weight

if current_pkg_weight > 0:
    packages_sent += 1
    pkg_unused = 20 - current_pkg_weight
    total_weight += current_pkg_weight

    if pkg_unused > max_unused:
        max_unused = pkg_unused
        max_unused_pkg_num = packages_sent

total_unused_capacity = (packages_sent * 20) - total_weight

print("\nNumber of packages sent: {}".format(packages_sent))
print("Total weight of packages sent: {} kg".format(total_weight))
print("Total 'unused' capacity: {} kg".format(total_unused_capacity))

if packages_sent > 0:
    print("Package with the most 'unused' capacity: Package {} (with {} kg unused)".format(
        max_unused_pkg_num,
        max_unused
    ))
else:
    print("No packages were sent.")