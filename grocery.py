def main():

    item_counts = {}

    while True:
        try:
            item = input().strip()
        except EOFError:
            break

        itemFormatted = item.upper()

        item_counts[itemFormatted] = item_counts.get(itemFormatted, 0) + 1

    for entry in sorted(item_counts):
        print(f"{item_counts[entry]} {entry}")


main()
