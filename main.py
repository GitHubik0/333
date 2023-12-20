import colorama

colorama.init()

print(colorama.Fore.BLUE + "Сині літери" + colorama.Fore.RESET)

print(colorama.Fore.BLACK + colorama.Back.WHITE + "Білий фон" + colorama.Back.RESET)

print(colorama.Style.BRIGHT + colorama.Fore.YELLOW + "Яскравий текст" + colorama.Style.RESET_ALL)

print(colorama.Fore.BLUE + "Сині літери" + colorama.Fore.RESET)

print(colorama.Fore.BLACK + colorama.Back.WHITE + "Білий фон" + colorama.Back.RESET)

print(colorama.Style.BRIGHT + colorama.Fore.YELLOW + "Яскравий текст" + colorama.Style.RESET_ALL)

colorama.deinit()
