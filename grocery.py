def main():

    list = {}

    while True:
        try:
            item = input()
        except EOFError:
            sorted_list = sorted(list)
            for entry in sorted_list:
                print(f"{list[entry]} {entry}")
            return

        itemFormatted = item.upper()

        if itemFormatted in list:
            list[itemFormatted] += 1
        else:
            list[itemFormatted] = 1


main()
